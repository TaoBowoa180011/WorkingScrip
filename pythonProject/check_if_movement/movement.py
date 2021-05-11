import cv2
import numpy as np
import os
from tqdm import tqdm
import json
from collections import deque
from shutil import copyfile
import traceback

location_files = os.listdir('video_frame_location')
location_files.sort()
for location_file in tqdm(location_files):
    if True:
        path = os.path.join("video_frame_location",location_file)
        print(location_file)
        foldername = location_file.split('_')[0]

        with open(os.path.join("video_frame_location",location_file),'r')as location_reader:
            file_content = json.load(location_reader)
        points = file_content['shapes'][0]['points']
        h = int(file_content['imageHeight'])
        w = int(file_content['imageWidth'])

        x1_src = float(points[0][0]/w)
        y1_src = float(points[0][1]/h)
        x2_src = float(points[1][0]/w)
        y2_src  = float(points[1][1]/h)
        if not os.path.isdir(foldername):
            continue
        videos = os.listdir(foldername)
        videos = [v for v in videos if v[-3:]=='mp4']
        for video in tqdm(videos):
            if True:
                cap = cv2.VideoCapture(os.path.join(foldername, video))
                success = True
                firstframe = ''
                errlist = []
                total = 0
                cnt_list = deque([], maxlen=20)
                cnt_list_all = []
                cnt_max_time = 10
                cnt_counter = 0
                print('processing %s'%os.path.join(foldername, video))
                while success:

                    if total % 2 == 0:
                        cap.set(cv2.CAP_PROP_POS_MSEC, total * 500)
                        success, frame = cap.read()
                        if len(firstframe) == 0:
                            firstframe = frame
                        else:
                            try:
                                # if frame is not None:
                                h, w, _ = frame.shape
                                # firstframe = frame
                                if firstframe.shape[0]!=frame.shape[0]:
                                    print('unequal')
                                    success = False

                                # for location in locations:
                                x1 = int(x1_src * w)
                                y1 = int(y1_src * h)
                                x2 = int(x2_src* w)
                                y2 = int(y2_src* h)

                                firstframe_location = firstframe[y1:y2, x1:x2]
                                firstframe_location = cv2.cvtColor(firstframe_location, cv2.COLOR_BGR2GRAY)
                                firstframe_location = cv2.GaussianBlur(firstframe_location, (21, 21), 0)

                                current_location = frame[y1:y2, x1:x2]
                                current_location = cv2.cvtColor(current_location, cv2.COLOR_BGR2GRAY)
                                current_location = cv2.GaussianBlur(current_location, (21, 21), 0)

                                frameDelta = cv2.absdiff(firstframe_location, current_location)
                                frameDelta_thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                                frameDelta_cnts, hierarchy = cv2.findContours(frameDelta_thresh.copy(),
                                                                              cv2.RETR_EXTERNAL,
                                                                              cv2.CHAIN_APPROX_SIMPLE)
                                # if total>500:
                                #     cv2.imshow('firstframe_location', firstframe_location)
                                #     cv2.imshow('current_location', current_location)
                                #     cv2.waitKey(0)
                                #     cv2.destroyAllWindows()

                                cnt_list_all.append(len(frameDelta_cnts))
                                cnt_list.append(len(frameDelta_cnts))
                                if np.average(cnt_list) > 3:

                                    if not os.path.exists(os.path.join(foldername, 'movement')):
                                        os.mkdir(os.path.join(foldername, 'movement'))
                                    copyfile(os.path.join(foldername, video), os.path.join(foldername, 'movement', video))
                                    success = False
                                    print('found %s'%video)

                            # except cv2.error:
                            #     firstframe = frame
                            #     traceback.print_exc()
                            #     pass
                            except:

                                # traceback.print_exc()
                                pass

                    total += 1
                print('total process frames %s'%total)





# for root,dirs,files in os.walk('.'):
#     dirs = [d for d in dirs if 'C' in d or 'E' in d or 'D' in d]
#     for d in dirs:
#         path = os.path.join(root, d)
#         mp4s = os.listdir(path)
#         for mp4 in tqdm(mp4s):
#             cap = cv2.VideoCapture(os.path.join(path, mp4))
#             success = True
#             firstframe = ''
#             errlist = []
#             total = 0
#             while success:
#                 total += 1
#
#                 if total % 2 == 0:
#                     cap.set(cv2.CAP_PROP_POS_MSEC, total * 500)
#                     success, frame = cap.read()
#                     if len(firstframe) == 0:
#                         firstframe = frame
#                     else:
#                         try:
#                             # if frame is not None:
#                             for location in locations:
#                                 x1 = int(location[0][0])
#                                 y1 = int(location[0][1])
#                                 x2 = int(location[1][0])
#                                 y2 = int(location[1][1])
#                                 firstframe_location = firstframe[y1:y2, x1:x2]
#                                 current_location = frame[y1:y2, x1:x2]
#                                 # firstframe = frame
#                                 err = mse(firstframe_location, current_location)
#                                 errlist.append(err)
#                                 # if err>5000:
#                                 #     if not os.path.exists(os.path.join(path,'movement')):
#                                 #         os.mkdir(os.path.join(path,'movement'))
#                                 #     copyfile(os.path.join(path, mp4),os.path.join(path,'movement',mp4))
#
#                                 if np.sum(errlist) / len(errlist) > 300:
#                                     print(mp4)
#                                     print(np.sum(errlist) / len(errlist))
#
#                                     # success=False
#                                     # print(mp4)
#                                     # print(total * 0.5)
#
#                             # cv2.imshow(mp4, frame)
#
#                         except:
#                             traceback.print_exc()
#                             print(success)
#                             pass