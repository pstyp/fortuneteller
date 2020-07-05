from flask import Response, render_template, request
import requests
from application import app, db
from application.models import Fortune


@app.route('/', methods=['GET'])
def home():
    fortuneData=Fortune.query.all()
    requests.get('')
    return render_template('home.html')
