"""
rtmp_show.py
Just shows RTMP stream from given address, until user hits 'Q' key
"""

import cv2
import time
stream_addr = 'rtmp://s3b78u0kbtx79q.cloudfront.net/cfx/st/honda_accord'
#stream_addr='rtmp://192.168.153.128:1935/stream/rtmptest live=1'
cap = cv2.VideoCapture(stream_addr)
fps_cnt=0
fps=0
flag=0
stime=-time.time()
img="./tmp/gen_"
while(True):
    fps_cnt+=1
    flag+=1
    ret, frame = cap.read()
    if(time.time()+stime>10):
        fps=fps_cnt/(time.time()+stime)
        fps_cnt=0
        stime=-time.time()
    #cv2.imshow('frame', frame)
    #print(frame)
    print("fps is:",fps)
    cv2.imwrite(img+str(flag)+".png",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
