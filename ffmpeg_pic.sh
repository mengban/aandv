#ffmpeg -probesize 32768 -i "rtmp://192.168.153.128:1935/stream/rtmptest live=1" -y -t 0.001 -ss 1 -f image2 -r 1 rtm3.jpeg 
ffmpeg -i "rtmp://192.168.153.128:1935/stream/rtmptest live=1" -f image2 -ss 0 -y -vframes 1 a.jpg

