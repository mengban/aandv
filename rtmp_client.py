import librtmp
import time
# Create a connection
conn = librtmp.RTMP("rtmp://192.168.153.128:1935/stream/rtmptest", live=True)
# Attempt to connect
conn.connect()
# Get a file-like object to access to the stream
stream = conn.create_stream()
# Read 1024 bytes of data
while True:
	time.sleep(1)
	data = stream.read(1024)
	print(data)
