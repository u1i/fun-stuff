data=data.src
if [ "$(grep gender $data)" = "" ]
then
    echo No face found
    exit
fi
. ./data.src

convert save.jpg   -gravity north -append \
          -gravity south \
          -stroke '#000C' -pointsize 50 -strokewidth 10 -annotate 0 "$emotion" \
          -stroke  none   -pointsize 50 -fill white    -annotate 0 "$emotion" \
          -gravity South -pointsize 24  -background Purple  -splice 0x30 -annotate +0+2 "$gender, $age, $glasses" \
          -fill none -stroke red -strokewidth 3 \
-draw "rectangle $face_left,$face_top $((face_left+face_width)),$((face_top+face_height))" \
-stroke green -strokewidth 3 -draw "circle $nosetip_x,$nosetip_y $((nosetip_x+2)),$nosetip_y" \
-draw "circle $pupil_left_x,$pupil_left_y $((pupil_left_x+2)),$pupil_left_y" \
-draw "circle $pupil_right_x,$pupil_right_y $((pupil_right_x+2)),$pupil_right_y" \
$emotion.png -gravity northwest   -geometry  +0+30 -composite \
out.jpg

convert out.jpg -geometry 192x108! emo_$emotion.jpg

