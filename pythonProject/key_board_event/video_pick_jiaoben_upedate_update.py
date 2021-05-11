import os
from tqdm import tqdm
import cv2
from moviepy.editor import VideoFileClip
filename='video_url3'
timeF=10
target_filename= '/home/zhen/Desktop/need_train_video/'

if not os.path.exists(target_filename):
    os.mkdir(target_filename)
for root,dirs,files in os.walk(filename):
    dirs.sort()
    for d in tqdm(dirs):
        if d[-1]=='t':
            continue
        flag=False
        video_all_time=0
        for r , dd , f in os.walk(os.path.join(filename,d)):
            f.sort()
            for file in f:
                cv2.destroyAllWindows()
                cv2.waitKey()
                if flag:
                    break
                print('filename: '+file)
                print('process: '+str(f.index(file))+'/'+str(len(f)))
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
                            if key == ord('s'):
                                flag = True
                                break
                            if key ==ord('a'):
                                clip = VideoFileClip(os.path.join(r,file))
                                print(clip.duration)
                                video_all_time+=float(clip.duration)
                                if not os.path.exists(os.path.join(target_filename,d)):
                                    os.mkdir(os.path.join(target_filename,d))
                                os.rename(os.path.join(r,file),os.path.join(os.path.join(target_filename,d),file))
                                print('save success, target path name: '+os.path.join(os.path.join(target_filename,d),file))
                                # print(os.path.join(r,file))
                                # print(os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                                # os.rename(os.path.join(r,file),os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                                if video_all_time>=600:
                                    flag = True
                                break
                        c += 1
                except:
                    vc.release()
                key2 = cv2.waitKey()
                if key2 == ord('a'):
                    clip = VideoFileClip(os.path.join(r, file))
                    print(clip.duration)
                    video_all_time += float(clip.duration)
                    if not os.path.exists(os.path.join(target_filename, d)):
                        os.mkdir(os.path.join(target_filename, d))
                    os.rename(os.path.join(r, file), os.path.join(os.path.join(target_filename, d), file))
                    print('save success, target path name: ' + os.path.join(os.path.join(target_filename, d), file))
                    # print(os.path.join(r,file))
                    # print(os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                    # os.rename(os.path.join(r,file),os.path.join(r,file.split('_')[0]+'_valid_'+str(ord_list.index(key))+'.mp4'))
                    if video_all_time >= 600:
                        flag = True
                    break
                cv2.destroyAllWindows()