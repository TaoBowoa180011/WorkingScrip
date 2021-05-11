import os
from tqdm import tqdm
import cv2
filename='/home/zhen/Desktop/need_to_CVAT/'
timeF=10
# target_filename= '/home/zhen/Desktop/video_target_update/'
ord_list = [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9')]

for root,dirs,files in os.walk(filename):
    dirs.sort()
    for d in tqdm(dirs):
        flag=False
        for r , dd , f in os.walk(os.path.join(filename,d)):
            f.sort()
            for file in f:
                cv2.waitKey()
                cv2.destroyAllWindows()
                if flag:
                    break
                print(file)
                vc=cv2.VideoCapture(os.path.join(os.path.join(filename,d),file))

                if vc.isOpened():
                    rval , frame = vc.read()
                else:
                    rval = False
                    print('can not read frame , filename is :'+file)

                c=1
                try:
                    while rval:
                        rval, frame = vc.read()
                        if (c % timeF == 0):
                            cv2.imshow(file,frame)
                            key = cv2.waitKey(10)
                            if key in ord_list:
                                # print(os.path.join(r,file))
                                print(os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                                os.rename(os.path.join(r,file),os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                                flag = True
                                break
                        c += 1
                except:
                    vc.release()
                key2=cv2.waitKey()
                if key2 in ord_list:
                    os.rename(os.path.join(r, file), os.path.join(r, file.split('_')[0] + '_valid_' + str(ord_list.index(key2)) + '.mp4'))
                    flag = True
                    break
                cv2.destroyAllWindows()