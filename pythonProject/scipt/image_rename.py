import os
path = '/home/zhen/images/meter/seg/meter_after_crop'

list_files = os.listdir(path)
for i ,file in enumerate(list_files):
    print(file)
    file_name = file.split('.')[0]
    if file_name[]