data=data.src

if [ "$(grep GENDER $data)" = "" ]
then
    echo No face found
    exit
fi

. ./data.src

convert save.jpg -gravity south \
          -stroke '#000C' -pointsize 24 -strokewidth 2 -annotate 0 "$gender, $age, $glasses - $emotion" \
          -stroke  none   -pointsize 24 -fill white    -annotate 0 "$gender, $age, $glasses - $emotion" \
          -fill none -stroke red -strokewidth 3 \
-draw "rectangle $face_left,$face_top $((face_left+face_width)),$((face_top+face_height))" \
-stroke green -strokewidth 3 -draw "circle $nosetip_x,$nosetip_y $((nosetip_x+2)),$nosetip_y" \
-draw "circle $pupil_left_x,$pupil_left_y $((pupil_left_x+2)),$pupil_left_y" \
-draw "circle $pupil_right_x,$pupil_right_y $((pupil_right_x+2)),$pupil_right_y" \
out.jpg
