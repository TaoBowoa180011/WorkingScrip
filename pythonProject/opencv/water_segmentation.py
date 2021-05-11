import cv2
import numpy as np
import torch


torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='/home/zhen/Desktop/LargePots2.pt')


img = cv2.imread('chess.jpeg',0)
blur = cv2.GaussianBlur(img,(3,3),0)
ret,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
ret,th1 = cv2.threshold(blur,200,255,cv2.THRESH_BINARY)

cv2.imshow('img',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)


cv2.waitKey(0)

