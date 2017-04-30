echo Capturing Cam...
# trap 'exit 130' INT
trap finish INT

function finish
{
	rm save.jpg 2>/dev/null
	rm image.jpg 2>/dev/null
	rm snaps/*
	killall imagesnap
	echo Bye
	exit

}

mkdir snaps 2>/dev/null
./take-snapshots-osx.sh&

while [ 1 ]
do
	convert snaps/$(ls -t snaps | head -1) -geometry 50% save.jpg
	# cp snaps/$(ls -t snaps | head -1) save.jpg
	./analyze_face.py save.jpg shell > data.txt
	./gen_image.sh
	mv out.jpg image.jpg 2>/dev/null
done
