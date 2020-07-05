from application import app
from flask import request, Response
import random



@app.route('/letter2', methods=['GET', 'POST'])
def letter2():
    letters2=['X', 'Y']
    return Response(letters2[random.randint(0,1)], mimetype='text/plain')
