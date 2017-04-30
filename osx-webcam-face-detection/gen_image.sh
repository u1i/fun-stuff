data=data.txt

if [ "$(grep GENDER $data)" = "" ]
then
    echo No face found
    exit
fi

age=$(grep AGE $data | head -1 | sed "s/AGE://;")
glasses=$(grep GLASSES $data | head -1 | sed "s/GLASSES://;")
gender=$(grep GENDER $data | head -1 | sed "s/GENDER://;")
face_top=$(grep FACE_TOP $data | head -1 | sed "s/FACE_TOP://;")
face_left=$(grep FACE_LEFT $data | head -1 | sed "s/FACE_LEFT://;")
face_width=$(grep FACE_WIDTH $data | head -1 | sed "s/FACE_WIDTH://;")
face_height=$(grep FACE_HEIGHT $data | head -1 | sed "s/FACE_HEIGHT://;")
emotion=$(grep EMOTION $data | head -1 | sed "s/EMOTION://;")
nosetip_x=$(grep NOSETIP_X $data | head -1 | sed "s/NOSETIP_X://;")
nosetip_y=$(grep NOSETIP_Y $data | head -1 | sed "s/NOSETIP_Y://;")

pupil_left_x=$(grep PUPIL_LEFT_X $data | head -1 | sed "s/PUPIL_LEFT_X://;")
pupil_left_y=$(grep PUPIL_LEFT_Y $data | head -1 | sed "s/PUPIL_LEFT_Y://;")
pupil_right_x=$(grep PUPIL_RIGHT_X $data | head -1 | sed "s/PUPIL_RIGHT_X://;")
pupil_right_y=$(grep PUPIL_RIGHT_Y $data | head -1 | sed "s/PUPIL_RIGHT_Y://;")


echo $age

#convert save.jpg -fill none -stroke red -strokewidth 3 -draw "rectangle $face_top,$face_left $face_width,$face_height" out.jpg
# convert save.jpg -fill none -stroke red -strokewidth 3 \
# -draw "rectangle $face_left,$face_top $((face_left+face_width)),$((face_top+face_height))" out.jpg

convert save.jpg -gravity south \
          -stroke '#000C' -pointsize 24 -strokewidth 2 -annotate 0 "$gender, $age, $glasses - $emotion" \
          -stroke  none   -pointsize 24 -fill white    -annotate 0 "$gender, $age, $glasses - $emotion" \
          -fill none -stroke red -strokewidth 3 \
-draw "rectangle $face_left,$face_top $((face_left+face_width)),$((face_top+face_height))" \
-stroke green -strokewidth 3 -draw "circle $nosetip_x,$nosetip_y $((nosetip_x+2)),$nosetip_y" \
-draw "circle $pupil_left_x,$pupil_left_y $((pupil_left_x+2)),$pupil_left_y" \
-draw "circle $pupil_right_x,$pupil_right_y $((pupil_right_x+2)),$pupil_right_y" \
out.jpg
