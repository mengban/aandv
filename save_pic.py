#import os
#os.system('ffmpeg -i "rtmp://192.168.153.128:1935/stream/rtmptest live=1" -f image2 -ss 0 -y -vframes 1 a.jpg')
import cv2
cv2.namedWindow("camCapture")
cap = cv2.VideoCapture()
sta=cap.open('"rtmp://192.168.153.128:1935/stream/rtmptest live=1"')
if not sta:
    print ("Not open")
while (True):
    print('start',sta)
    err,img = cap.read()
    print(img)
    if img and img.shape != (0,0):
        cv2.imwrite("img1", img)
        cv2.imshow("camCapture", img)
        print(img)
    if err:
        print (err)
        break
    cv2.waitKey(5)
