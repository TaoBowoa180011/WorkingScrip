import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
Source = '/home/zhen/Downloads/PotsClassify/1_0'
Target1 = '/home/zhen/Downloads/PotsClassify/1_0'
Target2 = '/home/zhen/Downloads/PotsClassify/1_1'
Target3 = '/home/zhen/Downloads/PotsClassify/1_3'
# Initialize the ORB detector algorithm
orb = cv2.ORB_create()
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

Source_list = os.listdir(Source)
Target1_list = os.listdir(Target1)
Target2_list = os.listdir(Target2)
Target3_list = os.listdir(Target3)

for s in Source_list:
    path_s  = os.path.join(Source,s)
    imgS = cv2.imread(path_s)
    imgS_gray = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
    kpS, desS = orb.detectAndCompute(imgS_gray, None)
    if type(desS) is np.ndarray:
        for t in Target1_list:
            path_T1 = os.path.join(Target1,t)
            imgT1 = cv2.imread(path_T1)
            imgT1_gray = cv2.cvtColor(imgT1, cv2.COLOR_BGR2GRAY)
            kpT1, desT1 = orb.detectAndCompute(imgT1_gray, None)
            if type(desT1) is np.ndarray:
                matches_ST1 = bf.match(desS,desT1)
                #matches_ST1 = sorted(matches_ST1, key = lambda x: x.distance)
                print((matches_ST1[0]))

                #sim_ST1 = sum(matches_ST1[:])

            #print(sim_ST1)


