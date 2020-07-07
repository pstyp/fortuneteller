from flask import Response, render_template, request
import requests
from application import app, db
from application.models import Fortune


@app.route('/', methods=['GET'])
def home():
    fortuneData=Fortune.query.all()
    response=requests.get("http://service4:5003/fortune")
    textresp=response.text
    return render_template('home.html', title='Homepage', fortune=fortuneData, textresp=textresp)
