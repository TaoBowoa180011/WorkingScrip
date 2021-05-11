import os
import cv2
import numpy as np
import random
global dstfolder
from tqdm import tqdm
filename="unzip/"
mse_fa=500

def mse(a,b):
    try:
        err = np.sum((a.astype("float")-b.astype("float"))**2)
        err /= float(a.shape[0]* a.shape[0])
    except:
        err=0

    return err


def judgement_class(objlocation,picture_name,output_name):
    im = cv2.imread(picture_name)
    h, w, _ = im.shape
    objlocation = [float(i) for i in objlocation]
    x1 = int((float(objlocation[0]) * w))
    y1 = int((float(objlocation[1]) * h))
    xw = int((float(objlocation[2])) * w / 2)
    xh = int((float(objlocation[3])) * h / 2)
    crop_img = im[y1 - xh:y1 + xh, x1 - xw:x1 + xw]
    cv2.imwrite(output_name, crop_img)

def return_picture(context_2,picture_name):
    im = cv2.imread(picture_name)
    h, w, _ = im.shape
    if type(context_2) ==str:
        objlocation = context_2.split(" ")[1:]
    else:
        objlocation=context_2
    objlocation = [float(i) for i in objlocation]
    x1 = int((float(objlocation[0]) * w))
    y1 = int((float(objlocation[1]) * h))
    xw = int((float(objlocation[2])) * w / 2)
    xh = int((float(objlocation[3])) * h / 2)
    crop_img = im[y1 - xh:y1 + xh, x1 - xw:x1 + xw]
    return  crop_img,  objlocation




for root,dir,files in os.walk(filename):
    for d in  tqdm(dir):
        if d[-4:]=='data':
            continue
        if d.split('_')[3][0] in ['1', '4']:
            dstfolder = "location_dataset/1-4/"
        if d.split('_')[3][0] in ['2', '3', '6']:
            dstfolder = "location_dataset/2-3-6/"
        if d.split('_')[3][0] == '5':
            dstfolder = "location_dataset/5/"
        if d[-4:]=='data':
            continue
        orign_lid=[]
        orign_sink=[]
        '''start set orign'''
        with open(filename+ d + '/obj_train_data/frame_000000.txt') as orign_txt:
            orign_contexts = orign_txt.readlines()
        for orign_context in orign_contexts:
            if orign_context[0] in ['0','1','3']:
                orign_lid.append(return_picture(orign_context,filename+ d + '/obj_train_data/frame_000000.PNG'))
            if orign_context[0] in ['2','4']:
                orign_sink.append(return_picture(orign_context,filename + d + '/obj_train_data/frame_000000.PNG'))
        # print(len(orign_sink))
        # print(orign_lid)
        """start all folder"""
        # print(orign_sink)
        mse_lid_list_same=[]
        mse_lid_list_diff=[]
        mse_sink_list_same = []
        mse_sink_list_diff = []
        for r, d1, f in os.walk(filename+ d+'/obj_train_data'):

            for f1 in f:
                if f1[-1] == 'G':
                    if orign_sink:
                        for orign_sink_location in orign_sink:
                            # print(orign_sink_location)
                            crop_img,objlocation=return_picture(orign_sink_location[1],
                                                                filename+ d+'/obj_train_data/'+f1)
                            mse_sink_result=mse(orign_sink_location[0],crop_img)
                            if mse_sink_result <= mse_fa:
                                mse_sink_list_same.append([mse_sink_result,crop_img,f1])
                            else:
                                mse_sink_list_diff.append([mse_sink_result,crop_img,f1])
                    if orign_lid:
                        for orign_lid_location in orign_lid:
                            crop_img,objlocation=return_picture(orign_lid_location[1],
                                                                filename + d + '/obj_train_data/' + f1)
                            mse_lid_result=mse(orign_lid_location[0],crop_img)
                            if mse_lid_result <= mse_fa:
                                mse_lid_list_same.append([mse_lid_result,crop_img,f1])
                            else:
                                mse_lid_list_diff.append([mse_lid_result,crop_img,f1])

        if len(mse_sink_list_same)>=20:
            mse_sink_list_same=random.sample(mse_sink_list_same,20)
        if len(mse_sink_list_diff)>=40:
            mse_sink_list_diff=random.sample(mse_sink_list_diff,40)

        if len(mse_lid_list_same)>=20:
            mse_lid_list_same=random.sample(mse_lid_list_same,20)
        if len(mse_lid_list_diff)>=40:
            mse_lid_list_diff=random.sample(mse_lid_list_diff,40)

        for sink_output in mse_sink_list_same+mse_sink_list_diff:
            # print('location_dataset/sink/'+d+sink_output[2])
            cv2.imwrite('location_dataset/sink/'+d+sink_output[2],sink_output[1])
        for lid_output in mse_lid_list_same+mse_lid_list_diff:
            cv2.imwrite(dstfolder + d + lid_output[2], lid_output[1])
        # list1=random.sample(list(filter(lambda x:x[0]>3000,mse_sink_list)),10)
        # print(list1)
        # print(len(mse_lid_list))
        # sinkresult=random.sample((filter(lambda x:x[0]>3000,mse_sink_list)),10)
        # print(len(sinkresult))


        # for r, d1, f in os.walk("unzip/" + d + '/obj_train_data'):
        #     for f1 in f:
        #         if f1[-1] == 't':
        #             with open("unzip/" + d + '/obj_train_data/' + f1) as txt:
        #                 contexts_2 = txt.readlines()
        #
        #             # if d.split('_')[3][0] not in ['1','2','3','4','5','6']:
        #             #     print(d)
        #             if not os.path.isdir(dstfolder):
        #                 os.mkdir(dstfolder)
        #             for context_2 in contexts_2:
        #                 if context_2[0] in ['0','1','3']:
        #
        #                     if len( flag_init_lib) == 0:
        #                         flag_init_lib=judgement_class(context_2,"unzip/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG',dstfolder+d+'_lidopen_'+f1[0:-4]+'.PNG')
        #
        #
        #                     else:
        #                         now_lib=return_picture(context_2,"unzip/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG')
        #                         mse_lib_list.append([f1[0:4],mse(origin_lib,now_lib)])
        #
        #                 if context_2[0] in ['2','4']:
        #                     sinklocation='location_dataset/sink/'
        #                     if not os.path.isdir(sinklocation):
        #                         os.mkdir(sinklocation)
        #
        #                     if len(flag_init_sink) == 0:
        #                         flag_init_sink=judgement_class(context_2,"unzip/"+d+'/obj_train_data/'+f1[0:-4]+'.PNG',sinklocation+d+'_lidopenwithobj_'+f1[0:-4]+'.PNG')
        #
        #                     else:
        #                         now_sink = return_picture(context_2,"unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG')
        #                         mse_sink_list.append([f1[0:4], mse(origin_lib, now_sink)])
        # flag+=1
        # print(float(flag)/float(len(dir)))
        # # print(d.split('_')[3][0])
        # if d.split('_')[3][0] in ['1', '4']:
        #     dstfolder = "location_dataset/1-4/"
        # if d.split('_')[3][0] in ['2', '3', '6']:
        #     dstfolder = "location_dataset/2-3-6/"
        # if d.split('_')[3][0] == '5':
        #     dstfolder = "location_dataset/5/"
        # if d.split('_')[3][0] not in ['1', '2', '3', '4', '5', '6']:
        #     continue