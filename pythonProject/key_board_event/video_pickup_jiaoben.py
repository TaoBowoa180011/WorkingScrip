import os
from tqdm import tqdm
import cv2
filename='/home/zhen/Desktop/movement/'
timeF=10
target_filename= '/home/zhen/Desktop/need_to_CVAT/'



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
                print('filename: ' + file)
                print('process: ' + str(f.index(file)) + '/' + str(len(f)))
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
                            if key == ord('a'):
                                target_filename_dir=os.path.join(target_filename,d)
                                if not os.path.isdir(target_filename_dir):
                                    os.mkdir(target_filename_dir)
                                os.rename(os.path.join(r,file),os.path.join(target_filename_dir,file[:-4]+'.mp4'))
                                print('save success, target path name: '+os.path.join(os.path.join(target_filename,d),file))
                                flag = True
                                break
                            if key ==ord('s'):
                                flag = True
                                break
                        c += 1
                except:
                    vc.release()
                key2=cv2.waitKey()
                if key2 == ord('a'):
                    target_filename_dir = os.path.join(target_filename, d)
                    if not os.path.isdir(target_filename_dir):
                        os.mkdir(target_filename_dir)
                    os.rename(os.path.join(r, file), os.path.join(target_filename_dir, file[:-4] + '.mp4'))
                    print('save success, target path name: ' + os.path.join(os.path.join(target_filename, d), file))
                    flag = True
                    break
                cv2.destroyAllWindows()