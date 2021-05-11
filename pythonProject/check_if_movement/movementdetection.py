import os
import cv2
import time
import numpy as np
from tqdm import tqdm
from shutil import copyfile
ref_point = []
import matplotlib.pyplot as plt
import traceback


# construct the argument parser and parse the arguments


def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))

        # draw a rectangle around the region of interest
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)


        with open(path+'/locations.txt','a') as locationstxt:
            locationstxt.write(str(ref_point))
            locationstxt.write('\n')
        cv2.imshow(d, image)
# load the image, clone it, and setup the mouse callback function
# image = cv2.imread(img)
def mse(a, b):
    err = np.sum((a.astype("float") - b.astype("float")) ** 2)
    err /= float(a.shape[0] * a.shape[0])

    return err

    # keep looping until the 'q' key is pressed
def movementdetection(locations,mp4s):
    for mp4 in tqdm(mp4s):
        cap = cv2.VideoCapture(os.path.join(path, mp4))
        success = True
        firstframe = ''
        errlist = []
        total = 0
        while success:
            success,frame = cap.read()
            total+=1

            if  len(firstframe)==0:
                firstframe = frame
            else:
                try:
                    # if frame is not None:
                    for location in locations:
                        x1 =int(location[0][0])
                        y1 =int(location[0][1])
                        x2 =int(location[1][0])
                        y2 =int(location[1][1])
                        firstframe_location = firstframe[y1:y2, x1:x2]
                        current_location = frame[y1:y2, x1:x2]
                        firstframe = frame
                        err = mse(firstframe_location,current_location)
                        if err>5000:
                            if not os.path.exists(os.path.join(path,'movement')):
                                os.mkdir(os.path.join(path,'movement'))
                            copyfile(os.path.join(path, mp4),os.path.join(path,'movement',mp4))
                            errlist.append(err)

                            success=False
                except:
                    traceback.print_exc()

                    pass
        # if np.std(errlist)>1000:
        #     copyfile(os.path.join(path, mp4), os.path.join(path, 'movement', mp4))
        # plt.xlabel('Smarts')
        # plt.ylabel(np.var(errlist))
        # plt.axis([0, 10000,0,8000])
        # plt.title(mp4)
        #
        # plt.plot(range(0,len(errlist)), errlist, 'r--', linewidth=1)
        # plt.grid(True)
        #
        # plt.show()

for root,dirs,files in os.walk('..'):
    dirs = [d for d in dirs if 'C' in d or 'E' in d or 'D' in d]
    for d in dirs:
        path = os.path.join(root,d)
        mp4s = os.listdir(path)
        mp4s = [mp4 for mp4 in mp4s if mp4[-3:]=='mp4']
        firstmp4 = mp4s[0]
        first_cap = cv2.VideoCapture(os.path.join(path,firstmp4))
        locations = []
        while True:
            success,frame = first_cap.read()
            if success:
                image = frame

                clone = image.copy()
                cv2.namedWindow(d)
                cv2.setMouseCallback(d, shape_selection)
                while True:
                    # display the image and wait for a keypress
                    cv2.imshow(d, image)
                    key = cv2.waitKey(1) & 0xFF

                    # press 'r' to reset the window
                    if key == ord("r"):
                        image = clone.copy()

                    # if the 'c' key is pressed, break from the loop
                    elif key == ord("c"):
                        with open(path + '/locations.txt', 'r') as locationsread:
                            locationfromfile = locationsread.readlines()
                        for line in locationfromfile:
                            locations.append( list(eval(line)))
                        movementdetection(locations,mp4s)
                        break

                # close all open windows
                cv2.destroyAllWindows()

            break