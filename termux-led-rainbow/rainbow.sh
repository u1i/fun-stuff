sleep 5
for col in FF0000 E2571E FF7F00 FFFF00 00FF00 96bf33 0000FF 4B0082 8B00FF ffffff

do

echo rb | termux-notification --led-color $col --led-on  1000 --led-off  0

done
