from flask import request, Response, render_template
import requests
from application import app, db
from application.models import Fortune


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    letter1=requests.get('http://service2:5001/letter1')
    letter2=requests.get('http://service3:5002/letter2')
    code=letter1.text+letter2.text
    if code=='AX':
        fortune='(大吉): great blessing'
        fort_code=Fortune(
                code=code,
                fortune=fortune
                )
        db.session.add(fort_code)
        db.session.commit()
        return code+' ⇒ '+fortune
    elif code=='AY':
        fortune='(吉): blessing'
        fort_code=Fortune(
                code=code,
                fortune=fortune
                )
        db.session.add(fort_code)
        db.session.commit()
        return code+' ⇒ '+fortune
      
    elif code=='BX':
        fortune='(凶): curse'
        fort_code=Fortune(
                code=code,
                fortune=fortune
                )
        db.session.add(fort_code)
        db.session.commit()
        return code+' ⇒ '+fortune
    else:
        fortune='(大凶): great curse'
        fort_code=Fortune(
                code=code,
                fortune=fortune
                )
        db.session.add(fort_code)
        db.session.commit()
        return code+' ⇒ '+fortune
    

