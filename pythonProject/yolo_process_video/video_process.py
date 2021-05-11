from intelab_python_sdk.logger import log,log_init
from datetime import datetime, timedelta
# import classification
from tqdm import tqdm
from PIL import Image
import pandas as pd
import numpy as np
import traceback
# import detection
import requests
import random
import config
import time
import json
import cv2
import os


class Video_Process():


    def download_with_url(self, url, store_path, filename):
        start_download_time = time.time()

        if not os.path.isdir(store_path):
            os.makedirs(store_path)
        if not os.path.exists(store_path + filename):
            try:
                r = requests.get(url, allow_redirects=True)
                open(store_path + filename, 'wb').write(r.content)
                end_download_time = time.time()
                download_duration = end_download_time-start_download_time

                log.info("download %s finished from %s seconds time using %s seconds"% (filename, url, str(int(download_duration))))
            except Exception as e:

                print(e)
                traceback.print_exc()

    def get_sink_locations_vcap(self,vcap,yolo,device_id,filename):
        cout = 0

        fps = int(vcap.get(cv2.CAP_PROP_FPS))
        success = True
        while success:
            success, frame = vcap.read()
            if success:
                if cout % (10 * fps) == 0:
                    yolo_sample_path = 'inference/tmp/' + device_id + "/yolo_sample/"
                    if not os.path.exists(yolo_sample_path + filename + ".png"):
                        if not os.path.isdir(yolo_sample_path):
                            os.makedirs(yolo_sample_path)
                        sink_location = yolo.detect(frame, filename, True, yolo_sample_path)
                    else:
                        sink_location = yolo.detect(frame, device_id)

                    if any([x[0] == 'sink' for x in sink_location]):
                        log.info("sink locations found: " + str(sink_location))

                        return sink_location

                if cout >= 3 * fps * 10:
                    break

                cout += 1
        return

    def get_sink_locations(self, group,yolo):
        for index, row in group.iterrows():
            device_id = row[0]
            url = row[1]
            filename = row[1].split("/")[-1]

            # if first. get location of sinks
            store_path = "inference/tmp/" + device_id + "/videos/"
            self.download_with_url(url, store_path, filename)

            vcap = cv2.VideoCapture(store_path+ filename)
            sink_location = self.get_sink_locations_vcap(vcap,yolo,device_id,filename)
            return sink_location
        return False
        # total_frames = vcap.get(7)

    @staticmethod
    def mse(a, b):
        err = np.sum((a.astype("float") - b.astype("float") )**2)
        err /= float(a.shape[0] * a.shape[0])

        return err

    def process(self,url):

        df = pd.read_csv(url,header=None)
        groups = df.groupby([0])

        yolo = detection.yoloInference()

        efficientnet_classes = ["1_0", "1_1", "1_3", "2_0", "2_1", "2_3", "3_0", "3_1", "3_3", "4_0", "4_1", "4_3", "5_0", "5_1", "5_3","7_1", "hand", "nohand"]
        efficientnet = classification.ClassificationInference(efficientnet_classes, efficientnet_classes)
        start = time.time()
        total_frames = 0
        total_frames_process_time = 0
        total_download_time = 0
        total_sink_cal_time = 0

        # for each device

        for idx, group in tqdm(groups):

            group[2] = pd.DatetimeIndex(pd.to_datetime(group[2])) + timedelta(hours=8, minutes=00)

            group = group.sort_values(by=2, ascending=True)
            group = group.reset_index()

            log.info("processing device %s " % (group[0][0]))

            locations = ''
            if config.location_update_frequency=='id':
                start_sink_location_time = time.time()

                locations = self.get_sink_locations(group,yolo)


                end_sink_location_time = time.time()
                sink_location_duration = end_sink_location_time - start_sink_location_time
                total_sink_cal_time+=sink_location_duration
                log.info("sink location calculating time: %s"% str(int(sink_location_duration)))


            if not locations and config.location_update_frequency=='id':
                continue

            log.info("efficientnet_classificing")
            out_json = {}

            out_json["deviceID"] = group[0][0]
            out_json["videos"] = []

            start_time_perdevice = time.time()

            # for each video
            for index, row in group.iterrows():
                device_id = row[0]
                url = row[1]
                filename = row[1].split("/")[-1]

                log.info("processing video "+ filename)

                store_path = "inference/tmp/" + device_id + "/"

                json_store_path = "inference/tmp/" + device_id + "/"
                video_store_path = store_path + "/videos/"+ filename

                video_results = {}
                video_results["video_name"] = filename
                video_results["url"] = str(url)
                video_results["video_start_time"] = str(row[2])
                video_results["video_end_time"] = str(row[3])

                video_results["results"] = []



                # if device_id == "132530765":
                #     break
                try:
                    download_path = store_path + "/videos/"
                    self.download_with_url(url, download_path, filename)

                    if os.path.exists(video_store_path):
                        vcap = cv2.VideoCapture(video_store_path)
                    else:
                        vcap = cv2.VideoCapture(url)

                    if config.location_update_frequency == 'video':
                        start_sink_location_time = time.time()

                        locations = self.get_sink_locations_vcap(vcap, yolo, device_id, filename)

                        end_sink_location_time = time.time()
                        sink_location_duration = end_sink_location_time - start_sink_location_time
                        total_sink_cal_time += sink_location_duration
                        log.info("sink location calculating time: %s" % str(int(sink_location_duration)))
                    if not locations and config.location_update_frequency == 'video':
                        continue

                    if config.location_update_frequency == 'id':
                        yolo_sample_path = 'inference/tmp/%s/yolo_sample/'%device_id
                        yolo_sample_path_filename = os.listdir(yolo_sample_path)
                        if len(yolo_sample_path_filename)==1:
                            yolo_sample_path_filename = yolo_sample_path_filename[0]
                            video_results["yolo_sample_image"] = yolo_sample_path+yolo_sample_path_filename
                        else:
                            video_results["yolo_sample_image"] = ''
                    elif config.location_update_frequency == 'video':
                        yolo_sample_path = 'inference/tmp/%s/yolo_sample/' % device_id
                        if os.path.exists(yolo_sample_path+filename+'.PNG'):
                            yolo_sample_path_filename = filename+'.PNG'
                            video_results["yolo_sample_image"] = yolo_sample_path + yolo_sample_path_filename
                        else:
                            video_results["yolo_sample_image"] = ''


                    for locations_idx, location in enumerate(locations):
                        video_results["results"].append(
                            {
                                "object_idx": locations_idx,
                                "object_type": location[0],
                                "coordinates": [location[1], location[2]],
                                "predictions": {}
                            }
                        )

                    fps = int(vcap.get(cv2.CAP_PROP_FPS))

                    video_results["fps"] = fps

                    length = int(vcap.get(cv2.CAP_PROP_FRAME_COUNT))

                    predictions = {}
                    success = True


                    start_classifying_time = time.time()

                    first_frame = None

                    cout = 0
                    previous_pot = ''

                    delete_TO = 1
                    wait_until = datetime.now() + timedelta(minutes=delete_TO)
                    break_loop = False
                    while success and not break_loop:

                        if cout % 2 == 0:
                            vcap.set(cv2.CAP_PROP_POS_MSEC, cout*1000)
                            success, frame = vcap.read()
                            if frame is not None and first_frame is None:
                                first_frame = frame

                            if len(video_results["results"]) > 0 and frame is not None:
                                images = []
                                for obj in video_results["results"]:
                                    object_idx = obj["object_idx"]
                                    obj_tp, obj_br = obj["coordinates"]

                                    obj_crop_image = frame[obj_tp[1]:obj_br[1], obj_tp[0]:obj_br[0]]
                                    first_frame_obj_crop_image = first_frame[obj_tp[1]:obj_br[1], obj_tp[0]:obj_br[0]]
                                    immse = self.mse(obj_crop_image, first_frame_obj_crop_image)
                                    if immse>1000:
                                        # cv2.imshow("first_frame_obj_crop_image",first_frame_obj_crop_image)
                                        # cv2.imshow("obj_crop_image",obj_crop_image)
                                        #
                                        # cv2.waitKey(800)
                                        # cv2.destroyAllWindows()

                                        obj_crop_image_save = obj_crop_image
                                        obj_crop_image = cv2.cvtColor(obj_crop_image, cv2.COLOR_BGR2RGB)
                                        obj_crop_image = Image.fromarray(obj_crop_image)

                                        images.append((obj_crop_image,object_idx))

                                if len(images)>0:
                                    object_type_idxs = [object_idxs[1] for object_idxs in images]
                                    images = [image[0] for image in images]
                                    images_save = images
                                    images = efficientnet.image_loader(images)
                                    preds = efficientnet.inference(images)


                                    for pred_idx, pred in enumerate(preds):

                                        object_type_index = object_type_idxs[pred_idx]
                                        object_type = video_results["results"][object_type_index]["object_type"]
                                        if object_type == 'sink':
                                            pred_class = efficientnet_classes[next(p for p in pred if p in [16, 17])]
                                            if pred_class == 'hand':
                                                hand_save_sample = images_save[pred_idx]
                                                if not os.path.isdir("inference/tmp/" + device_id + "/hand_samples/"):
                                                    os.makedirs("inference/tmp/" + device_id + "/hand_samples/")
                                                hand_save_sample.save(
                                                    "inference/tmp/" + device_id + "/hand_samples/" + "sink_" + filename + "_" + str(
                                                        object_type_index) + "_" + str(cout) + ".PNG")
                                                # hand_save_sample.show()
                                                # print(hand_save_sample.shape)
                                                #
                                                # hand_save_sample = np.moveaxis(hand_save_sample, 0, -1)
                                                # print(hand_save_sample.shape)
                                                #
                                                # cv2.imshow("obj_crop_image",hand_save_sample)
                                                #
                                                # cv2.waitKey(0)
                                                # cv2.destroyAllWindows()

                                        else:
                                            pred_class = efficientnet_classes[next(p for p in pred if p not in [16, 17])]
                                            if pred_class != previous_pot:
                                                hand_save_sample = images_save[pred_idx]
                                                if not os.path.isdir("inference/tmp/" + device_id + "/pot_samples/"):
                                                    os.makedirs("inference/tmp/" + device_id + "/pot_samples/")
                                                hand_save_sample.save(
                                                    "inference/tmp/" + device_id + "/pot_samples/" + "pot_" + filename + "_" + str(
                                                        object_type_index) + "_" + str(cout) + ".PNG")
                                            previous_pot = pred_class

                                        video_results["results"][object_type_index]["predictions"][cout] = pred_class

                        cout += 1
                        if wait_until < datetime.now() :
                            break_loop = True


                    end_classifying_time = time.time()
                    classifying_duration = end_classifying_time-start_classifying_time
                    total_frames+=cout
                    total_frames_process_time+=int(classifying_duration)
                    log.info("finished classifying %s time spend %s seconds total frames %s"% (filename, str(int(classifying_duration)), str(cout)))
                    log.info("")

                except Exception as e:
                    print(e)
                    traceback.print_exc()
                    pass


                out_json["videos"].append(video_results)

                with open(store_path + 'result.json', 'w') as outfile:
                    json.dump(out_json, outfile)

            end_time_perdevice = time.time()
            perdevice_process_duration = end_time_perdevice- start_time_perdevice
            log.info("finish processing device %s using %s seconds" % (group[0][0], str(int(perdevice_process_duration))))
        # end = time.time()
        # print(end - start)
        # print("total_frames_process_time %s"% str(total_frames_process_time))
        # print("total_frames %s"% str(total_frames))
        # print("total_sink_cal_time %s"% str(total_sink_cal_time))


if __name__ == '__main__':
    log = log_init('test', debug=True, log_path='./logs')

    videoProcess = Video_Process()
    for date in ['20','21']:
        videoProcess.process("url_2020-11-"+date+".txt")





