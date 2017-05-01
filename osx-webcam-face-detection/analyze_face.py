#!/usr/bin/python

import os
import sys
import json
import requests

# Azure endpoint and access key
endpoint="southeastasia.api.cognitive.microsoft.com"

# Add your own here
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

# get the emotion with the highest score
emotion_guess = max(json_data[0]["faceAttributes"]["emotion"], key=json_data[0]["faceAttributes"]["emotion"].get)

if output_mode == "json":
	print json_data[0]
else:
	print "export age=" + str(int(json_data[0]["faceAttributes"]["age"]))
	print "export gender=" + str(json_data[0]["faceAttributes"]["gender"])
	print "export glasses=" + str(json_data[0]["faceAttributes"]["glasses"])
	print "export emotion=" + str(emotion_guess)
	print "export face_top=" + str(json_data[0]["faceRectangle"]["top"])
	print "export face_left=" + str(json_data[0]["faceRectangle"]["left"])
	print "export face_width=" + str(json_data[0]["faceRectangle"]["width"])
	print "export face_height=" + str(json_data[0]["faceRectangle"]["height"])
	print "export pupil_left_x=" + str(int(json_data[0]["faceLandmarks"]["pupilLeft"]["x"]))
	print "export pupil_left_y=" + str(int(json_data[0]["faceLandmarks"]["pupilLeft"]["y"]))
	print "export pupil_right_x=" + str(int(json_data[0]["faceLandmarks"]["pupilRight"]["x"]))
	print "export pupil_right_y=" + str(int(json_data[0]["faceLandmarks"]["pupilRight"]["y"]))
	print "export nosetip_x=" + str(int(json_data[0]["faceLandmarks"]["noseTip"]["x"]))
	print "export nosetip_y=" + str(int(json_data[0]["faceLandmarks"]["noseTip"]["y"]))
