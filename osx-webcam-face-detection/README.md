# Realtime Face Detection

An (almost) realtime facial anaylysis camera that shows age, gender of a person, points out where eyes and nose are on the face and makes a guess about the emotional expression on the face.

![](https://github.com/u1i/fun-stuff/blob/master/osx-webcam-face-detection/sample.jpg?raw=true)

## Requirememts
* MacBook with a Python environment
* ImageMagick (via brew)
* Azure Face API subscription
* imagesnap

## How to use

1. Install imagesnap and ImageMagick - using brew
2. Get an Azure subscription for the [Cognitive Services Face API](https://www.microsoft.com/cognitive-services/en-us/face-api) and add it to the file analyze_face.py
3. open a terminal and run ./capture.sh in there
4. it's your choice which webserver you want to have, here we're using a simple Python wrapper, you can run ./start_server.sh in a second terminal window (I run both commands in the same window using [screen](https://www.gnu.org/software/screen/)
5. open [http://localhost:8080](http://localhost:8080) and try it out!
