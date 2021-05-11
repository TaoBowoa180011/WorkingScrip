import re
import os
import csv
import requests
import os
import cv2
import numpy as np
from shutil import copyfile
import shutil
import json
import random
import math
from PIL import Image


# from matplotlib import pyplot as plt
# os.system("cd ~/PycharmProjects")
# for root,dir,files in os.walk("work_done_zip"):
#     for f in files:
#
# #         os.rename(os.path.join(root,f),os.path.join(root,f.split(" ")[0])+".zip")
#         dirname = f.split(".")[0][:-2]
#         f1=f.split(' ')[0]
#         f2=f.split(' ')[1]
#         # print(dirname)
#         # os.mkdir('unzip/'+dirname)
#         # os.system("mkdir "+"unzips_classify/"+"/".join(os.path.join(root,dirname).split("/")[1:]))
#         print("unzip "+  os.path.join(root,f1+'\\'+' '+f2) + " -d " +"unzip/"+"/".join(os.path.join(root,dirname).split("/")[1:])+'/')
#         os.system("unzip "+  os.path.join(root,f1+'\\'+' '+f2) + " -d " +"unzip/"+"/".join(os.path.join(root,dirname).split("/")[1:])+'/')
# flag=0
# for root,dir,files in os.walk("unzip/"):
#     for d in dir:
#         if len(d) > 20:
#             # with open('unzip/'+d+'/obj.names','r') as objname:
#             #         context=objname.readlines()
#             for r , d1 ,f in os.walk("unzip/"+d+'/obj_train_data'):
#                 for f1 in f:
#                     if f1[-1]=='t':
#                        with open("unzip/"+d+'/obj_train_data/'+f1) as txt:
#                             contexts = txt.readlines()
#                        for context in contexts:
#                             if context[0]=='4':
#                                 flag+=1
#                                 break
#                     breakZ
# print(flag)
            #                         # print("unzip/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG')
            #                         im = cv2.imread("unzip/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG')
            #                         h, w, _ = im.shape
            #                         objlocation = context.split(" ")[1:]
            #                         objlocation = [float(i) for i in objlocation]
            #                         x1 = int((float(objlocation[0]) * w))
            #                         y1 = int((float(objlocation[1]) * h))
            #                         xw = int((float(objlocation[2])) * w / 2)
            #                         xh = int((float(objlocation[3])) * h / 2)
            #                         crop_img = im[y1 - xh:y1 + xh, x1 - xw:x1 + xw]
            #                         # cv2.imshow('1',crop_img)
            #                         # cv2.waitKey()
            #                         dstfolder = "class/" +d+ "/" +f1[0:-4]+'.PNG'
            #                         # print(dstfolder)
            #
            #                         if not os.path.isdir("class/" +d+ "/"):
            #                                 os.mkdir( "class/" +d+ "/")
            #                         cv2.imwrite(dstfolder, crop_img)
            # flag+=1
            # print(float(flag)/float(len(dir)))
total=0
for root,dir,files in os.walk("valid_lid"):
    print(dir)
    total+=len(files)
print(total)