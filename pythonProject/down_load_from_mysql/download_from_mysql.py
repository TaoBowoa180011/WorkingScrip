import os
from tqdm import tqdm
import random
import pandas as pd
import json

def file_list_2():
    '''second valid'''
    filename='/home/zhen/Desktop/CVAT_DOWNLOAD'
    all_valid=[]
    for root,dir,files in os.walk(filename):
        valid_file=list(filter(lambda x:x.split('_')[2]=='valid',dir))
    for file in valid_file:
        all_valid.append(file.split('_')[1].upper())
    return all_valid

def file_list_1():
    '''first valid'''
    filename = 'firstbatch_id.txt'
    all_filename=[]
    with open(filename,'r') as txt:
        filnamelist=txt.readlines()
    for filename in filnamelist:
        all_filename.append(filename[:-1])
    return all_filename

def file_list_3():
    filelist=file_list_1()+file_list_2()
    return filelist

def file_list_4():
    '''third shai'''
    global all_file_1
    filename= '/home/zhen/Desktop/wash_room'
    for root,dir,files in os.walk(filename):
        crop_files=[]
        # print(len(files))
        for f in files:
            crop_files.append(f.split('_')[0])
        print(crop_files)
        all_file_1= list(set(crop_files)-set(file_list_3()))
    return all_file_1

def file_list_5():
    filename='work_done_zip/'
    all_filelist=[]
    for root, dir, files in os.walk(filename):
        for f in files:
            all_filelist.append(f.split('_')[1].upper())
    # print(all_filelist)
    # print(len(all_filelist))
    return all_filelist
# print(len(file_list_4()))
def file_list_6():
    fillist= list(set(file_list_4())-set(file_list_5()))
    random_list=random.sample(fillist,22)
    file=pd.read_table('url_2020-11-20.txt',names=['name','url','time1','time2'],sep=' ',delimiter=',')
    # print(file['name'])
    # print(file['url'])
    urllist=[]
    for name in random_list:
        for key in list(file[file['name']==name]['url']):
            urllist.append(key)
            break
    print(len(urllist))
    if len(urllist) <20:
        return []
    else:
        return urllist
def file_list_7():
    '''wash room sun huai'''
    with open('traceback_list_need_done') as txt:
        contexts = txt.readlines()
    contexts=[i.rstrip('\n').rstrip() for i in contexts ]
    return file_list_7()




def file_list_8():
    filename = '/home/zhen/Desktop/video_target_update'
    all_valid = []
    for root, dir, files in os.walk(filename):
        for d in dir:
            for r , dd ,fs in os.walk(os.path.join(filename,d)):
                for f in fs:
                    all_valid.append(str(f).split('_')[0])
    # for file in valid_file:
    #     all_valid.append(file.split('_')[1].upper())
    return all_valid

def file_list_9():
    all_file = list(set(file_list_4()) - set(file_list_8()))
    return all_file
print(len(file_list_4()))
print(len(file_list_8()))

file_list_9()
print(len(file_list_9()))
with open('washroom_have_been_download.json') as txt:
    json.dump(file_list_9(),txt)

# print(len(list(set(file_list_4())-set(file_list_5()))))