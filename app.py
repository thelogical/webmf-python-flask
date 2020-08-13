#!/usr/bin/env python
import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')  # this route is not working
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'


@app.route('/version')
def getvers():
    return 'The version is 2.01'

@app.route('/hour/')
def getdate():
    k = datetime.datetime.now()
    return 'The hour is ' + str(k.hour)

@app.route('/add/<a>/<b>')
def add(a,b):
    
    try:
        sm = int(a) + int(b)
        return str(sm)
    except:
        return "The url should only be in format /add/a/b where a and b are strictly numbers"

@app.route('/sub/<a>/<b>')
def sub(a,b):

    try:
        sm = int(a) - int(b)
        return str(sm)
    except:
        return "The url should only be in format /add/a/b where a and b are strictly numbers"


@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    # show the user profile for that user
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1997)  # open for everyone
