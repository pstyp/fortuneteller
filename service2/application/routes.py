from application import app
from flask import request, Response
import random


@app.route('/letter1', methods=['GET', 'POST'])
def letter1():
    letters1=['A', 'B', 'C']
    return Response(letters1[random.randint(0,2)], mimetype='text/plain')
