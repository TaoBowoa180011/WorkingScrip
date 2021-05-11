import cv2
import numpy as np

pot_1 = cv2.imread('flip_task_c90842488_valid_5-2021_01_15_06_35_05-yolo_5_3_frame_004350.PNG')
pot_2 = cv2.imread('flip_task_c90842488_valid_5-2021_01_15_06_35_05-yolo_5_3_frame_006050.PNG')
pot_3 = cv2.imread('flip_task_c90842488_valid_5-2021_01_15_06_35_05-yolo_5_3_frame_006900.PNG')

pot_1_edges = cv2.Canny(pot_1,100,200)
print(pot_1_edges.shape)
print(pot_1_edges.sum()/255)
# kernel = np.ones((3,3),np.uint8)
pot_1_edges_dilate = cv2.dilate(pot_1_edges,None)
pot_1_edges_erode = cv2.erode(pot_1_edges_dilate,None)
cv2.imshow('pot_1',pot_1)
cv2.imshow('pot_1_edges',pot_1_edges)
cv2.imshow('pot_1_edges_dilate',pot_1_edges_dilate)
cv2.imshow('pot_1_edges_erode',pot_1_edges_erode)




pot_2_edges = cv2.Canny(pot_2,100,200)
print(pot_2_edges.sum()/255)
# kernel = np.ones((3,3),np.uint8)
# pot_2_edges_dilate = cv2.dilate(pot_2_edges,kernel)
# pot_2_edges_close = cv2.erode(pot_2_edges_dilate,kernel)
cv2.imshow('pot_2',pot_2)
cv2.imshow('pot_2_edges',pot_2_edges)
#cv2.imshow('pot_2_edges_dilate',pot_2_edges_dilate)
#cv2.imshow('pot_2_edges_close',pot_2_edges_close)

pot_3_edges = cv2.Canny(pot_3,100,200)
print(pot_3_edges.sum()/255)
#kernel = np.ones((3,3),np.uint8)
#pot_3_edges_dilate = cv2.dilate(pot_3_edges,kernel)
#pot_3_edges_close = cv2.erode(pot_3_edges_dilate,kernel)
cv2.imshow('pot_3',pot_3)
cv2.imshow('pot_3_edges',pot_3_edges)
#cv2.imshow('pot_3_edges_dilate',pot_3_edges_dilate)
#cv2.imshow('pot_3_edges_close',pot_3_edges_close)
cv2.waitKey(0)