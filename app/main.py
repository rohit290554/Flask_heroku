import json
import requests
from flask import Flask as flask, render_template, request

app = flask(__name__, template_folder='templates')


@app.route('/')
def my_form():
    return render_template('Home.html')


@app.route("/", methods=['GET', 'POST'])
def home_view():
    # form = cgi.FieldStorage()
    # external_ip = form.getvalue('text')
    ipur = 'https://ipapi.co/'
    ipurr = '/json/'
    # external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    external_ip = request.form['external_ip']
    print('Target IP Addr is : ' + external_ip)
    # ip_address = external_ip
    # URL to send the request to
    request_url = ipur + external_ip + ipurr
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    test = json.dumps(result)
    print(test)
    print(external_ip)
    return render_template('op.html', text=test)


@app.route("/ip")
def index():
    ip_address = request.remote_addr
    return "Requester IP: " + ip_address

