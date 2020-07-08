import unittest
from unittest.mock import patch

from flask import url_for, request, redirect, render_template
from flask_testing import TestCase

from application import app, db
from application.models import Fortune
from os import getenv



class TestBase(TestCase):

    def create_app(self):
        config_name='testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE'),
                DEBUG=True
                )
        return app


    def setUp(self):
       # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        db.session.commit()


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()



class TestPosts(TestBase):
   def test_db(self):
        fortune1=Fortune(code='AX', fortune='(大吉): great blessing')
        db.session.add(fortune1)
        db.session.commit()
        fortune=Fortune.query.all()
        assert repr(fortune)=='[Code: AX\r\nFortune: (大吉): great blessing\r\nID: 1\r\n]'
   
   
   
   def test_fortune(self):
      # letter1=requests.get('http://service2:5001/letter1').text
      # letter2=requests.get('http://service3:5002/letter2').text
       with patch("requests.get") as g:
           g.side_effect.text=['A','X']
           response=self.client.get(url_for('fortune'))
           self.assertIn(b'AX', response.data)
