import os
import cv2
import numpy as np
import random
global dstfolder
from tqdm import tqdm
filename='unziptest/'




for root,dir,files in os.walk(filename):
    for d in  tqdm(dir):
        if d[-4:]=='data':
            continue
        if d.split('_')[3][0] in ['1', '4']:
            dstfolder = "location_dataset_filter/1-4/"
        if d.split('_')[3][0] in ['2', '3', '6']:
            dstfolder = "location_dataset_filter/2-3-6/"
        if d.split('_')[3][0] == '5':
            dstfolder = "location_dataset_filter/5/"
        if d[-4:]=='data':
            continue
        orign_lid=[]
        orign_sink=[]

        with open(filename+ d + '/obj_train_data/frame_000000.txt') as orign_txt:
            orign_contexts = orign_txt.readlines()
        for orign_context in orign_contexts:
            if orign_context[0] in ['0','1','3']:
                orign_lid.append(return_picture(orign_context,filename+ d + '/obj_train_data/frame_000000.PNG'))
            if orign_context[0] in ['2','4']:
                orign_sink.append(return_picture(orign_context,filename + d + '/obj_train_data/frame_000000.PNG'))

