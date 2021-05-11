import os
def GetDeviceID(path):
    index_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            ind = f.split('_')
            for i in ind:
                if len(i) > 8 and i[0] not in ['s','f','r','S','F','R'] and '.' not in i and '-' not in i :
                    if i != 'd00000000':
                      index_list.append(i)

        id = list(dict.fromkeys(index_list))
        return id


id = GetDeviceID("/home/zhen/test_yolov5_pots/images")
print(id)
print(len(id))









