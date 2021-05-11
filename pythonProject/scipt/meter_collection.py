import cv2
import time
import os
import schedule
urls = ['rtmp://rtmp01open.ys7.com/openlive/ac7cd65f8c2e414184840403a1692238.hd',
            'rtmp://rtmp01open.ys7.com/openlive/d73745a546254702b3cdc33b215b9edb.hd',
            'rtmp://rtmp01open.ys7.com/openlive/08dc4162f5fb49f9b53fb0c9af5ca242.hd',
            'rtmp://rtmp01open.ys7.com/openlive/ac7cd65f8c2e414184840403a1692238.hd',
            'rtmp://rtmp01open.ys7.com/openlive/78d9428ff1fe436cbf9f061d2e81acbb.hd',
            'rtmp://rtmp01open.ys7.com/openlive/e81fa2b9c6854ce689b974d4aa102fc6.hd',
            'rtmp://rtmp01open.ys7.com/openlive/b42dfdc68aa541edbc8968caa0a84457.hd',
            'rtmp://rtmp01open.ys7.com/openlive/d738fe104534431aaa5c97f5f7a63fb8.hd',
            'rtmp://rtmp01open.ys7.com/openlive/b4e8dd9a20d449f6977b75b06f74e0c7.hd',
            'rtmp://rtmp01open.ys7.com/openlive/7d1e774d0d4243f79c62a78307c32201.hd',
            'rtmp://rtmp01open.ys7.com/openlive/04010ebc117f4f61b4e66aea6c763e35.hd']
def img_clloect():
    strtime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    print(strtime)
    for i,url in enumerate(urls):
        vcap = cv2.VideoCapture(url)
        ret, frame = vcap.read()
        if frame is not None:
            frame_name = 'meter' + str(i) + strtime + '.png'
            file_path = os.path.join('/home/zhen/images/meter/seg',frame_name)
            # cv2.imshow('frame', frame)
            cv2.imwrite(file_path,frame)
        else:
            print('video is not valid')
        vcap.release()
    print('job is down')

schedule.every(30).minutes.do(img_clloect)

while True:
    schedule.run_pending()
    time.sleep(1)