import urllib.request

import requests
from flask import Flask as flask
import json

app = flask(__name__)


@app.route("/")
def home_view():
    ipur = 'https://ipapi.co/'
    ipurr = '/json/'
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print('Target IP Addr is : ' + external_ip)
    ip_address = external_ip
    # URL to send the request to
    request_url = ipur + external_ip + ipurr
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    test = json.dumps(result)
    print(test)
    return test


@app.route("/geoip")
def home_():
    return 'test'
