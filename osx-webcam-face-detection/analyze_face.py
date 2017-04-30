#!/usr/bin/python

import os
import sys
import json
import requests

# Azure endpoint and access key
endpoint="southeastasia.api.cognitive.microsoft.com"

azure_subscription_key=""

if len(sys.argv) < 3:
    sys.exit('Usage: %s <filename> [json|shell]' % sys.argv[0])

input_file = sys.argv[1]
output_mode = sys.argv[2]


request_url = "https://" + endpoint + "/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=age,gender,glasses,emotion"


headers = {'Content-type': 'application/octet-stream', 'Host': endpoint, 'Ocp-Apim-Subscription-Key': azure_subscription_key}
params = {'visualFeatures': 'Faces'}

with open(input_file, mode='rb') as file_handle:
    file_content = file_handle.read()

    response = requests.post(request_url, params=params, headers=headers, data=file_content)

vision=True
detected=True

# Did we get JSON back ?
try:
	json_data = json.loads(response.text)

except:
	vision=False

try:
    detect = json_data[0]["faceAttributes"]["age"]
except:
    exit(1)

#for emo in json_data[0]["faceAttributes"]["emotion"]:
# 	print emo
#	print json_data[0]["faceAttributes"]["emotion"][emo]

# get the emotion with the highest score
emotion_guess = max(json_data[0]["faceAttributes"]["emotion"], key=json_data[0]["faceAttributes"]["emotion"].get)

if output_mode == "json":
	print json_data[0]
else:
	print "AGE:" + str(json_data[0]["faceAttributes"]["age"])
	print "GENDER:" + str(json_data[0]["faceAttributes"]["gender"])
	print "GLASSES:" + str(json_data[0]["faceAttributes"]["glasses"])
	print "EMOTION:" + str(emotion_guess)
	print "FACE_TOP:" + str(json_data[0]["faceRectangle"]["top"])
	print "FACE_LEFT:" + str(json_data[0]["faceRectangle"]["left"])
	print "FACE_WIDTH:" + str(json_data[0]["faceRectangle"]["width"])
	print "FACE_HEIGHT:" + str(json_data[0]["faceRectangle"]["height"])
	print "PUPIL_LEFT_X:" + str(int(json_data[0]["faceLandmarks"]["pupilLeft"]["x"]))
	print "PUPIL_LEFT_Y:" + str(int(json_data[0]["faceLandmarks"]["pupilLeft"]["y"]))
	print "PUPIL_RIGHT_X:" + str(int(json_data[0]["faceLandmarks"]["pupilRight"]["x"]))
	print "PUPIL_RIGHT_Y:" + str(int(json_data[0]["faceLandmarks"]["pupilRight"]["y"]))
	print "NOSETIP_X:" + str(int(json_data[0]["faceLandmarks"]["noseTip"]["x"]))
	print "NOSETIP_Y:" + str(int(json_data[0]["faceLandmarks"]["noseTip"]["y"]))
