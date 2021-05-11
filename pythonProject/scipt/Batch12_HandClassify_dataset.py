import os
import random
import shutil
SrcPath = '/home/zhen/PycharmProjects/workingscripts/autocollection/Batch12nohand'
TargetPath = '/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classify_dataset2'
# files = os.listdir(SrcPath)
f_dict = {}
# for f in files:
#     key = f.split('_frame')[0]
#     f_dict[key] = []
# for f in files:
#     key = f.split('_frame')[0]
#     f_dict[key].append(f)
#
# print(f_dict.keys())
# for key in f_dict.keys():
#     file_list = f_dict[key]
#     l = len(file_list)
#     sample_list = random.sample(file_list,min(20,l))
#     print(sample_list)
#     for sample in sample_list:
#         src_path = os.path.join(SrcPath,sample)
#         trg_path = os.path.join(TargetPath,sample)
#         shutil.copyfile(src_path,trg_path)
files = os.listdir(SrcPath)
for f in files:
    key = f.split('_frame')[0]
    f_dict[key] = []
for f in files:
    key = f.split('_frame')[0]
    f_dict[key].append(f)
count = 0
train = []
val = []
for key in f_dict.keys():
    if count < len(f_dict.keys()) * 0.8:
        train.append(key)
    else:
        val.append(key)
    count += 1

print(train,len(train))
print(val,len(val))

for key in train:
    file_list = f_dict[key]
    for f in file_list:
        src_path = os.path.join(SrcPath,f)
        trg_path = os.path.join(TargetPath,'train/nohand')
        trg_path = os.path.join(trg_path,f)
        shutil.copyfile(src_path,trg_path)
for key in val:
    file_list = f_dict[key]
    for f in file_list:
        src_path = os.path.join(SrcPath,f)
        trg_path = os.path.join(TargetPath,'val/nohand')
        trg_path = os.path.join(trg_path, f)
        shutil.copyfile(src_path,trg_path)