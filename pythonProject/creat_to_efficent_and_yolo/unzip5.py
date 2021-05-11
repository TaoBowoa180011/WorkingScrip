import os
import cv2
import numpy as np

global dstfolder


def mse(a, b):
    err = np.sum((a.astype("float") - b.astype("float")) ** 2)
    err /= float(a.shape[0] * a.shape[0])

    return err


def judgement_class(context_2, picture_name, output_name):
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
    return crop_img


flag = 0
for root, dir, files in os.walk("unzip/"):
    for d in dir:
        if d[-1] != 'a':
            with open("unzip/" + d + '/obj.names') as t_xt:
                contexts = t_xt.readlines()
                for context in contexts:
                    if context == 'sink\n':
                        sink = contexts.index(context)
                    if context == 'lidopenwithobj\n':
                        lidopenwithobj = contexts.index(context)
                    if context == 'lidclose\n':
                        lidclose = contexts.index(context)
                    if context == 'lidopen\n':
                        lidopen = contexts.index(context)
                    if context == 'wash\n':
                        wash = contexts.index(context)

        for r, d1, f in os.walk("unzip/" + d + '/obj_train_data'):

            flag_init_sink = True
            flag_init_lib = True
            mselist = []

            for f1 in f:
                if f1[-1] == 't':
                    with open("unzip/" + d + '/obj_train_data/' + f1) as txt:
                        contexts_2 = txt.readlines()
                    # print(d.split('_')[3][0])
                    if d.split('_')[3][0] in ['1', '4']:
                        dstfolder = "location_dataset/1-4/"
                    if d.split('_')[3][0] in ['2', '3', '6']:
                        dstfolder = "location_dataset/2-3-6/"
                    if d.split('_')[3][0] == '5':
                        dstfolder = "location_dataset/5/"
                    if d.split('_')[3][0] not in ['1', '2', '3', '4', '5', '6']:
                        continue
                    # if d.split('_')[3][0] not in ['1','2','3','4','5','6']:
                    #     print(d)
                    if not os.path.isdir(dstfolder):
                        os.mkdir(dstfolder)
                    for context_2 in contexts_2:
                        if context_2[0] == str(lidopen):
                            if flag_init_lib == True:
                                origin_lib = judgement_class(context_2,
                                                             "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                                             dstfolder + d + '_lidopen_' + f1[0:-4] + '.PNG')
                                flag_init_lib = False
                            judgement_class(context_2, "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                            dstfolder + d + '_lidopen_' + f1[0:-4] + '.PNG')
                        if context_2[0] == str(lidclose):
                            if flag_init_lib == True:
                                origin_lib = judgement_class(context_2,
                                                             "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                                             dstfolder + d + '_lidclose_' + f1[0:-4] + '.PNG')
                                flag_init_lib = False
                            judgement_class(context_2, "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                            dstfolder + d + '_lidclose_' + f1[0:-4] + '.PNG')
                        if context_2[0] == str(lidopenwithobj):
                            if flag_init_lib == True:
                                origin_lib = judgement_class(context_2,
                                                             "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                                             dstfolder + d + '_lidopen_' + f1[0:-4] + '.PNG')
                                flag_init_lib = False
                            judgement_class(context_2, "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                            dstfolder + d + '_lidopenwithobj_' + f1[0:-4] + '.PNG')
                        if context_2[0] == str(sink):
                            sinklocation = 'location_dataset/sink/'
                            if not os.path.isdir(sinklocation):
                                os.mkdir(sinklocation)
                            if flag_init_sink == True:
                                origin_sink = judgement_class(context_2,
                                                              "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                                              sinklocation + d + '_lidopenwithobj_' + f1[0:-4] + '.PNG')
                                flag_init_sink = False
                            judgement_class(context_2, "unzip/" + d + '/obj_train_data/' + f1[0:-4] + '.PNG',
                                            sinklocation + d + '_lidopenwithobj_' + f1[0:-4] + '.PNG')
        flag += 1
        print(float(flag) / float(len(dir)))