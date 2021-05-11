import torch
import cv2
from .paddle_utils import parse_args, create_paddle_predictor
from .predict import predict
import os
def Padding(xyxy, height, width):
    if xyxy[0] - 10 < 0:
        xyxy[0] = 0
    else:
        xyxy[0] = xyxy[0] - 10

    if xyxy[1] - 10 < 0:
        xyxy[1] = 0
    else:
        xyxy[1] = xyxy[1] - 10

    if xyxy[2] + 10 > width:
        xyxy[2] = width
    else:
        xyxy[2] = xyxy[2] + 20

    if xyxy[3] + 10 > height:
        xyxy[3] = height
    else:
        xyxy[3] = xyxy[3] + 10

    return xyxy[0], xyxy[1], xyxy[2], xyxy[3]


args = parse_args()
Hand_classification = create_paddle_predictor(args)


model = torch.hub.load('ultralytics/yolov5', 'custom',\
                      path_or_model='/home/zhen/PycharmProjects/pythonProject/yolov5_1/sink_recognition/sink_yolo.pt')
video = cv2.VideoCapture('https://prod-jiandu-shanghai.oss-cn-shanghai.aliyuncs.com/D88628751_2021-03-17_00-27-03.mp4')
count = 0
while(True):
    ret, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if frame is not None:
        count += 1
        res = model(frame)
        img = res.imgs[0]
        #cv2.imshow('current img',img)
        h,w = img.shape[0],img.shape[1]
        cor = res.pred[0][:,0:4].tolist()
        #cor_with_padding = []
        for i in range(len(cor)):
            x1, y1, x2, y2 = Padding(cor[i], h, w)
            print(x1, y1, x2, y2)
            sink_crop = img[int(y1):int(y2), int(x1):int(x2)]
            classes_pred, scores_pred = predict(args, Hand_classification, sink_crop)
            img_name = '{0}_{1}_{2}.png'.format(count,classes_pred,i)
            img_path = os.path.join('/home/zhen/PycharmProjects/pythonProject/yolov5_1/sink_recognition/infer',img_name)
            #print(img_path)
            cv2.imwrite(img_path,sink_crop)

            #print('classes_pred',classes_pred)
            #print('scores_pred',scores_pred)
            #cv2.waitKey(0)
        if cv2.waitKey(22) & 0xFF == ord('q'):
                break
    else:
        print('video is over')
        break

video.release()

