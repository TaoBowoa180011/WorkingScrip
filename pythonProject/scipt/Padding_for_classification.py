import cv2
import os
import numpy as np
import ast


def Padding(xyxy, height, width):
    if xyxy[0] - 20 < 0:
        xyxy[0] = 0
    else:
        xyxy[0] = xyxy[0] - 20

    if xyxy[1] - 20 < 0:
        xyxy[1] = 0
    else:
        xyxy[1] = xyxy[1] - 20

    if xyxy[2] + 20 > width:
        xyxy[2] = width
    else:
        xyxy[2] = xyxy[2] + 20

    if xyxy[3] + 20 > height:
        xyxy[3] = height
    else:
        xyxy[3] = xyxy[3] + 20

    return xyxy[0], xyxy[1], xyxy[2], xyxy[3]

def Process(src,trg):
    for root, dirs, files in os.walk(src):
        for f in files:
            if f[-3:] == 'txt':
                txt_path = os.path.join(root, f)
                #print(txt_path)
                with open(txt_path, 'r') as TXT:
                    lines = TXT.readlines()
                    for line in lines:

                        try:
                            line = ast.literal_eval(line)
                            #print(line)
                            x1 = line[0][0]
                            y1 = line[0][1]
                            x2 = line[1][0]
                            y2 = line[1][1]
                            # for i in range(len(line)):
                            #     # x1 = line[i][0][0]
                            #     # y1 = line[i][0][1]
                            #     # x2 = line[i][1][0]
                            #     # y2 = line[i][1][1]
                            #     #print(x1, y1, x2, y2)
                            #     #xyxy = np.array([x1,y1,x2,y2], dtype=float)
                            # img
                            img_name = f[:-3] + 'jpg'
                            img_path = os.path.join(root, img_name)
                            if os.path.exists(img_path):
                                img = cv2.imread(img_path)
                                height, width, channels = img.shape

                                x1 = int(x1 * width)
                                y1 = int(y1 * height)
                                x2 = int(x2 * width)
                                y2 = int(y2 * height)
                                #print(x1,y1,x2,y2)
                                x1, y1, x2, y2 = Padding([x1, y1, x2, y2], height, width)
                                #print(x1, y1, x2, y2)
                                dir_name = img_name.split('-')[0]
                                dir_path = os.path.join(trg,dir_name)
                                if not os.path.exists(dir_path):
                                    os.mkdir(dir_path)
                                img_crop_path = os.path.join(dir_path, img_name)
                                cv2.imwrite(img_crop_path, img[y1:y2, x1:x2])

                        except SyntaxError:
                            pass


def main():
    Src = '/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classify_test_dataset/sink'
    Trg = '/home/zhen/PycharmProjects/workingscripts/autocollection/Handtest/sink'
    Process(Src,Trg)
    print("Process finished!")

if __name__ == "__main__":
    main()
