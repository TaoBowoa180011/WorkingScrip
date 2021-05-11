import os
import cv2
import torch
import shutil
import time

#model = torch.load('/home/zhen/Downloads/YOLO0305best.pt', map_location='cpu')
model = torch.hub.load('ultralytics/yolov5', 'custom',path_or_model='/home/zhen/Downloads/yolo_detect_ultrasonic.pt')  # custom model
with open('/home/zhen/PycharmProjects/pythonProject/yolov5_1/url.txt','r') as txt:
    lines = txt.readlines()
for f in lines:
    f = f.replace('"','')
    f = f.rstrip()

    cap = cv2.VideoCapture(f)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = model(frame)
    results.save()
    shutil.copyfile('results/image0.jpg',
                    'results/' + '%s-%s.jpg' % (
                        str('old'), round(time.time() * 1000)))
    #if cv2.waitKey(0) & 0xFF == ord('q'):
     #   break





    