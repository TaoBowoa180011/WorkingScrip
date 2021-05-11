import os
from tqdm import tqdm
import json
import cv2
filename = '/home/zhen/Desktop/yolo_inference_sink/'
to_filename = '/home/zhen/Desktop/yolo_bad_inference/'
need_train = '/home/zhen/Desktop/need_train_video/'



for root,dirs,files in os.walk(filename):
    files.sort()
    for f in tqdm(files):
        print(f)
        img = cv2.imread(os.path.join(root,f))
        dim = (1000, 600)
        imdisp = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow(f, imdisp)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        if key == ord('a'):
            os.rename(filename+f,to_filename+f)
        if key == ord('d'):
            continue
        cv2.destroyAllWindows()
# all_filename= []
# for root,dirs,files in os.walk(to_filename):
#     files.sort()
#     for f in tqdm(files):
#         all_filename.append(f.split('_')[0])
# print(len(all_filename))
# all_need_filename=[]
# for root,dirs,files in os.walk(need_train):
#     all_need_filename=dirs
#     break
# print(len(all_need_filename))
# need_again = list(set(all_filename) - set(all_need_filename))
# print(need_again)

# with open('need_copy_donw.json','w') as txt:
#     json.dump(all_filename,txt)
# os.mkdir('need_train_video')
# with open ('need_copy_donw.json','r') as txt:
#     allfilename_list= json.load(txt)
#
# for filename in allfilename_list:
#     print('cp -r '+str(filename)+' need_train_video/'+str(filename))
#     os.system('cp -r '+str(filename)+' need_train_video/'+str(filename))

