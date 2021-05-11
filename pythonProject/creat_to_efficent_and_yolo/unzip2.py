import os
import random
import cv2
import numpy as np
from shutil import copyfile
import shutil
import json
import random
import math
from PIL import Image
global sink
global lidopenwithobj
global lidclose
global lidopen
global wash


flag=0
def judgement_class(context_2,picture_name,output_name):
    im = cv2.imread(picture_name)
    h, w, _ = im.shape
    objlocation = context_2.split(" ")[1:]
    objlocation = [float(i) for i in objlocation]
    x1 = int((float(objlocation[0]) * w))
    y1 = int((float(objlocation[1]) * h))
    xw = int((float(objlocation[2])) * w / 2)
    xh = int((float(objlocation[3])) * h / 2)
    crop_img = im[y1 - xh:y1 + xh, x1 - xw:x1 + xw]
    cv2.imwrite(output_name, crop_img)



# for root,dir,files in os.walk("unziptest/"):
#     for d in dir:
#         if d[-1] !='a':
#             with open("unziptest/" + d + '/obj.names' ) as t_xt:
#                 contexts = t_xt.readlines()
#                 for context in contexts:
#                     if context=='sink\n':
#                         sink=contexts.index(context)
#                     if context=='lidopenwithobj\n':
#                         lidopenwithobj=contexts.index(context)
#                     if context=='lidclose\n':
#                         lidclose=contexts.index(context)
#                     if context=='lidopen\n':
#                         lidopen=contexts.index(context)
#                     if context=='wash\n':
#                         wash=contexts.index(context)
#
#         for r, d1, f in os.walk("unziptest/" + d + '/obj_train_data'):
#             for f1 in f:
#                 if f1[-1] == 't':
#                     with open("unziptest/" + d + '/obj_train_data/' + f1) as txt:
#                         contexts_2 = txt.readlines()
#                     dstfolder = "valid_lid/" + d + "/"
#                     if not os.path.isdir(dstfolder):
#                         os.mkdir(dstfolder)
#                     for context_2 in contexts_2:
#                         if context_2[0] == str(lidopen):
#                             judgement_class(context_2,"unziptest/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG',dstfolder+d+'_lidopen_'+f1[0:-4]+'.PNG')
#                         if context_2[0] == str(lidclose):
#                             judgement_class(context_2,"unziptest/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG',dstfolder+d+'_lidclose_'+f1[0:-4]+'.PNG')
#                         if context_2[0] == str(lidopenwithobj):
#                             judgement_class(context_2,"unziptest/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG',dstfolder+d+'_lidopenwithobj_'+f1[0:-4]+'.PNG')
#         flag+=1
#         print(float(flag)/float(len(dir)))
flagall=0
for root,dir,files in os.walk("valid_lid/"):
    for d in dir:
        print(d)
        dst = 'finalfile/' + d + '/'
        if not os.path.isdir(dst):
            os.mkdir(dst)

        if d.split('_')[2]=='invalid' and d.split('_')[3].split('-')[0][0] !='0':
            for r ,d1 ,fi in os.walk("valid_lid/"+d+'/'):
                fname=random.sample(fi,50)
                for ffname in fname:
                    print('cp /home/zhen/PycharmProjects/pythonProject/valid_lid/'+d+'/'+ffname+
                              ' /home/zhen/PycharmProjects/pythonProject/finalfile/'+d+'/')
                    os.system('cp /home/zhen/PycharmProjects/pythonProject/valid_lid/'+d+'/'+ffname+
                              ' /home/zhen/PycharmProjects/pythonProject/finalfile/'+d+'/')


        if d.split('_')[2]=='valid':
            for rr, dd1, ffi in os.walk("valid_lid/" + d + '/'):

                flag=0
                for ffii in ffi:
                    if ffii.split('_')[-3]=='lidopenwithobj' or ffii.split('_')[-3]=='lidopen':
                        os.system('cp /home/zhen/PycharmProjects/pythonProject/valid_lid/'+d+'/'+ffii+
                              ' /home/zhen/PycharmProjects/pythonProject/finalfile/'+d+'/')
                        flag+=1

                fname_close=random.sample(ffi,flag)
                for ffname_close in fname_close:
                    os.system('cp /home/zhen/PycharmProjects/pythonProject/valid_lid/' + d + '/' + ffname_close +
                              ' /home/zhen/PycharmProjects/pythonProject/finalfile/' + d + '/')
        flagall+=1
        print(float(flagall)/float(len(d)))
# print('cp /home/zhen/PycharmProjects/pythonProject/valid_lid' +' /home/zhen/PycharmProjects/pythonProject/finalfile/' +'/')