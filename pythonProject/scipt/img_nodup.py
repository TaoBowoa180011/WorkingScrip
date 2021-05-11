import cv2
import os
import numpy as np
import shutil
def mse(a, b):
    """
    calculate mse between image a and b
    :param a: image
    :param b: image
    :return: mse
    """
    err = np.sum((a.astype("float") - b.astype("float")) ** 2)
    err /= float(a.shape[0] * a.shape[0])

    return err
def main():
    files = os.listdir('/home/zhen/Desktop/b1_5_train/3_close')
    f_dict = {}

    for f in files:
        key = f.split('_frame')[0]
        f_dict[key] = []
    for f in files:
        key = f.split('_frame')[0]
        f_dict[key].append(f)
    # print(f_dict)

    for key in f_dict.keys():
        file_list = f_dict[key]
        file_list.sort()
        print('file_list:',len(file_list))
        nodup_list = file_list
        print('before nodup:', len(nodup_list))
        i = 0
        while (i < len(nodup_list)):
            imgA_source_path = os.path.join('/home/zhen/Desktop/b1_5_train/3_close', nodup_list[i])
            imgA = cv2.imread(imgA_source_path)
            #print(imgA_source_path)
            #cv2.imwrite(imgA_target_path, imgA)
            #nodup_list.append(file_list[i])
            j = i + 1
            while(j < len(nodup_list)):
                imgB_source_path = os.path.join('/home/zhen/Desktop/b1_5_train/3_close', nodup_list[j])
                #imgB_target_path = os.path.join('/home/zhen/Desktop/ultrasonic_0_classify/train/0_close', file_list[j])
                imgB = cv2.imread(imgB_source_path)
                try:
                    grayA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
                    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)
                    err = mse(grayA,grayB)
                    #print('err',err)
                except ValueError:
                    err = 0
                if err < 200:
                    #cv2.imwrite(imgB_target_path, imgB)
                    #dup_list.append(file_list[j])
                    nodup_list.pop(j)
                else:
                    j += 1
            i += 1
        print('after nodup:',len(nodup_list))
        for f in nodup_list:
            img_source_path = os.path.join('/home/zhen/Desktop/b1_5_train/3_close', f)
            img_target_path = os.path.join('/home/zhen/Desktop/ultrasonic_3_classify/train/3_close',f)
            shutil.copyfile(img_source_path,img_target_path)

if __name__ == "__main__":
    main()
    print("finished")




