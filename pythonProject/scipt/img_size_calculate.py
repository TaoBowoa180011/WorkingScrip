import os
import cv2
count = 0
h_sum = 0
w_sum = 0
for root,dirs,files in os.walk('/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classify_dataset2'):
    for f in files:
        img_path = os.path.join(root,f)
        img = cv2.imread(img_path)
        count += 1
        h,w = img.shape[0],img.shape[1]
        h_sum += h
        w_sum += w

h_mean = h_sum / count
w_mean = w_sum / count

print(count)
print(h_mean)
print(w_mean)