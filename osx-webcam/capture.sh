echo Capturing Cam...
# trap 'exit 130' INT
trap finish INT


function finish
{
	rm inew.jpg 2>/dev/null
	rm image.jpg 2>/dev/null
	echo Exiting
	exit

}

while [ 1 ]
do
	rm inew.jpg 2>/dev/null
	ffmpeg -r 30 -f avfoundation -i "0" -frames 1 inew.jpg >/dev/null 2>&1
	mv inew.jpg image.jpg 2>/dev/null
done
