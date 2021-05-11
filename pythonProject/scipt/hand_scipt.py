import os
import shutil
import random
Source_Path = '/home/zhen/PycharmProjects/workingscripts/autocollection/withpadding/nohand/sec_nohand'
Target_path = '/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classfiy_dataset_2/'
deviceList = os.listdir(Source_Path)
print(deviceList)
train_list = random.sample(deviceList,int(len(deviceList)*0.8))
val_list = [items for items in deviceList if items not in train_list]

# print(len(deviceList))
# print(len(train_list))
# print(len(val_list))
for device in train_list:
    device_path = os.path.join(Source_Path,device)
    files = os.listdir(device_path)
    for f in files:
        file_path = os.path.join(device_path,f)
        target = os.path.join(Target_path,'train/nohand')
        target = os.path.join(target, f)
        shutil.copyfile(file_path,target)

for device in val_list:
    device_path = os.path.join(Source_Path,device)
    files = os.listdir(device_path)
    for f in files:
        file_path = os.path.join(device_path,f)
        target = os.path.join(Target_path,'val/nohand')
        target = os.path.join(target,f)
        shutil.copyfile(file_path,target)