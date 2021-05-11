import requests
from six.moves import urllib
import os
import sys
import cv2
import pandas as pd
# from download_from_mysql import *

def download_and_extract(filepath, save_dir):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    for url , index in zip(filepath,range(len(filepath))):
        filename = url.split('/')[-1]
        if not os.path.isdir(os.path.join(save_dir, filename.split('_')[0])):
            os.makedirs(os.path.join(save_dir, filename.split('_')[0]))
        save_path = os.path.join(os.path.join(save_dir, filename.split('_')[0]),filename)
        urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
        sys.stdout.flush()

# download_and_extract(['https://prod-jiandu-shanghai.oss-cn-shanghai.aliyuncs.com/D81142877_2020-11-20_00-15-08.mp4'],'video_url/')
all_url=[]
for date in ['16']:
    with open ('url_2020-12-'+date+'.txt','r') as txt:
        txt_lines=txt.readlines()
    for txt_line in txt_lines:
        all_url.append(txt_line.split(',')[3])
    # print(len(all_url))
    all_url = list(set(all_url))

# download_and_extract(all_url,'video_url_12_16/')

file = pd.read_csv('url_2020-12-16.txt', header=None)
file=file.groupby(0)
print(list(file))




# with open('url_2020-12-16.txt','r') as txt:
#     contexts = txt.readlines()
#
#
# for context in contexts:
#     cap = cv2.VideoCapture(context.split(',')[3])
#     '''get width and height'''
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#     '''get start time and finish time'''
#     time_start = float(context.split(',')[1])
#     end_time = float(context.split(',')[2])
#     frame_id = 0
#     while(cap.isOpened()):
#         ret ,frame = cap.read()
#         if  float(time_start)<=cap.get(cv2.CAP_PROP_POS_MSEC)*1000<float(end_time):
#
#             frame_id +=1
