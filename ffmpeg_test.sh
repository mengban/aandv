foo=(
  'rtmp://192.168.153.128:1935/stream'
  #'playpath=mp4:foo.mp4'
  #'swfUrl=http://bar.com/baz.swf'
  'live=1'
)

ffmpeg -i "${foo[*]}" -r 1 a%d.png &

while sleep 1
do
  ls -I a.png | xargs -I % mv % a.png
done
