from flask import Flask
from datetime import datetime
import time
app = Flask(__name__)
@app.route("/")
def t():
    name = 'gal'
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    return '''
       <html>
    <head>
        <meta http-equiv="refresh" content="10" />
        <title>HTML in 10 Simple Steps or Less</title>
    </head>
    <body>
    <h2>{}, Current Time is: {}</h2>
    <img src="{{url_for('static', filename='gal.jpg')}}" align="middle" alt="fucking shit"/>
    </body>
    </html>
        '''.format(name,current)
@app.route("/gal")
def g():
    return '''<html><head><b>HAIDEEEE!!!!!</b></head></html>'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

