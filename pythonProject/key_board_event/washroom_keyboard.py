import cv2
import os
from tqdm import tqdm
from shutil import  move
vailddst = "/home/zhen/Desktop/wash_room/"
vailddst_unlid = "/home/zhen/Desktop/wash_room_unlid/"
invailddst = "/home/zhen/Desktop/un_wash_room/"
brokendst = "/home/zhen/Desktop/video_broken/"
un_xiaodu = "/home/zhen/Desktop/un_xiaodu/"
filename= "/home/zhen/Desktop/useway_1_needtofilter/"



def dealwith_picture(filename):
    """本函数为将所有视频中提取关键帧并保存"""
    vc=cv2.VideoCapture(filename)

    if vc.isOpened():
        rval , frame = vc.read()
    else:
        rval = False
        print('ure')
    try:
        while rval:
            rval, frame =vc.read()
            cv2.imwrite('test.jpg',frame)
            break
    except:
        vc.release()

for root,dirs,files in os.walk(filename):
    files.sort()
    for f in tqdm(files):
        print(f)
        dealwith_picture(filename+f)
        img = cv2.imread('test.jpg')
        srcpath = 'test.jpg'

        # scale_percent = 100
        # width = int(img.shape[1] * scale_percent / 100)
        # height = int(img.shape[0] * scale_percent / 100)
        dim = (1000, 600)
        imdisp = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        cv2.imshow(f, imdisp)
        key = cv2.waitKey(0)
        if key == ord('a'):
            os.rename(filename+f,vailddst+f)
        elif key == ord('d'):
            os.rename(filename+f,invailddst+f)
        elif key == ord('w'):
            os.rename(filename+f,brokendst+f)
        elif key == ord('q'):
            os.rename(filename+f,vailddst_unlid+f)
        elif key == ord('s'):
            os.rename(filename+f,un_xiaodu+f)
        cv2.destroyAllWindows()
        # for d in dirs:
        #     for rs, ds, fs in os.walk(os.path.join(root,d)):
        #         print(fs)
        #         fs.sort()
        #         print(fs)
        #         for file in fs:
        #             if file[-3:] == "PNG":
        #                 img = cv2.imread(os.path.join(rs, file))
        #                 srcpath = os.path.join(rs, file)
        #
        #                 scale_percent = 500
        #                 width = int(img.shape[1] * scale_percent / 100)
        #                 height = int(img.shape[0] * scale_percent / 100)
        #                 dim = (width, height)
        #                 imdisp = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #
        #                 cv2.imshow("result", imdisp)
        #                 key = cv2.waitKey(0)
        #
        #                 if key == ord(' '): # pass to valid
        #                     path = "unzips_classify/sink_wash_valid/"+d+"/"
        #                     donepath = donedst+"/"+d+"/"
        #                     if not os.path.isdir(donepath):
        #                         os.mkdir(donepath)
        #                     if not os.path.isdir(path):
        #                         os.mkdir(path)
        #                     cv2.imwrite(path+file,img)
        #                     move(srcpath,donepath+file)
        #
        #                     print("move to valid" + "    "+ path+file)
        #
        #                 elif key == ord('d'): # pass to invalid
        #                     path = "unzips_classify/sink_wash_invalid/" + d+"/"
        #                     donepath = donedst+"/"+d+"/"
        #                     if not os.path.isdir(donepath):
        #                         os.mkdir(donepath)
        #                     if not os.path.isdir(path):
        #                         os.mkdir(path)
        #                     cv2.imwrite(path + file, img)
        #                     move(srcpath,donepath+file)
        #                     print("move to invalid" + "    "+ path+file)
