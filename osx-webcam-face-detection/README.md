# Face Detection Photo Booth

A facial anaylysis camera that shows age, gender of a person, highlights eyes and nose on the face and makes a guess about the emotional expression of the person - in (almost) real time!

![](https://github.com/u1i/fun-stuff/blob/master/osx-webcam-face-detection/sample.jpg?raw=true)

## What it does

* captures images from your webcam, one each second
* uses a neural network on the cloud to analyze the face - age, gender, emotion, landmarks
* adds the information to the image and displays it

## Some more technical details

* image capturing: there's many ways to do that, you can also use ffmpeg to do the task, I've also experimented with Droidcam (Android phone). Anything that gets you a constant stream of JPGs will do.
* OSX is not Linux. Setting up Python and ImageMagick might be a bit trickier there.
* ImageMagick needs fonts, they don't always work right away on OSX. See [this link here](http://stackoverflow.com/questions/32421233/imagemagick-fonts-not-found-in-osx) how to fix it
* image rendering is done in a separate shell-script. Once I figure out how to get the ImageMagick bindings working on Python/OSX we can combine this into one. Probably also a good idea to explore doing this with containers
* index.html is a very basic page that uses JavaScript (not my strong side) to reload the images every second. Does it well enough but this could be done much nicer I guess.
* this is really meant as a demo / prototype to show the concept. In a real solution you'd want a real time video stream, where the information is rendered into it using JavaScript. Help me to make this better!


## Requirememts
* MacBook with a Python environment. Libraries: requests, json
* ImageMagick (via brew)
* Azure Face API subscription
* imagesnap

## How to use this demo

1. Install imagesnap and ImageMagick - using brew
2. Get an Azure subscription for the [Cognitive Services Face API](https://www.microsoft.com/cognitive-services/en-us/face-api) and add it to the file analyze_face.py
3. open a terminal and run ./capture.sh in there
4. it's your choice which webserver you want to have, here we're using a simple Python wrapper, you can run ./start_server.sh in a second terminal window (I run both commands in the same window using [screen](https://www.gnu.org/software/screen/)
5. open [http://localhost:8080](http://localhost:8080) and try it out!
