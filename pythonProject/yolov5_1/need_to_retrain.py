import cv2
import os
def Check_Image(Path):
    ID_list = {}
    for root, dirs, files in os.walk(Path):

        for f in files:

            file_path = os.path.join(root,f)
            deviceID = f.split('_')[0]
            img = cv2.imread(file_path)
            cv2.imshow(deviceID, img)

            k = cv2.waitKey(0)
            if k == ord("s"):  # saveID
                if deviceID not in ID_list.keys():
                    ID_list[deviceID] = 1
                else:
                    ID_list[deviceID] += 1
                cv2.destroyWindow(deviceID)
            if k == ord("c"): #close windows
                cv2.destroyWindow(deviceID)
            if k == 27:  # Esc
                break
    return ID_list

id = Check_Image("/pythonProject/yolov5_1/need_to_retrain/exp3")
print(id)
