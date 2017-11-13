from bottle import default_app, route, request
from random import randint
import json

import pycurl
from StringIO import StringIO

@route('/geo')
def geo():

    try:
        lat = request.query['lat']
    except:
        lat = "-1"

    try:
        lon = request.query['lon']
    except:
        lon = "-1"

    try:
        map = request.query['map']
    except:
        map = "-1"

    # Call what3words API to get geolocation

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://api.what3words.com/v2/reverse?coords=' + lat + ',' + lon + '&key=__YOUR_KEY__&lang=en&format=json&display=full')
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    data = json.loads(body)
    res = data['words']

    # Cal IFTTT to save in Google Sheet

    buffer2 = StringIO()
    c2 = pycurl.Curl()
    c2.setopt(c2.URL, 'https://maker.ifttt.com/trigger/__TRIGGERNAME__/with/key/__YOUR_KEY__?value1=' + lat + ',' + lon + '&value2=' + res + '&value3=' + map + '')
    c2.setopt(c2.WRITEDATA, buffer2)
    c2.perform()
    c2.close()

    return "Geo Service " + lat + " " + lon + " " + map + " " + res

application = default_app()


