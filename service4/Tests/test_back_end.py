import unittest
from unittest.mock import patch
import requests_mock
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
   
   
   def test_fortune_1(self):
      # letter1=requests.get('http://service2:5001/letter1').text
      # letter2=requests.get('http://service3:5002/letter2').text
        with requests_mock.mock() as m:
           m.get('http://service2:5001/letter1', text='A')
           m.get('http://service3:5002/letter2', text='X') 
           response = self.client.get(url_for('fortune'))
           self.assertIn(b'AX', response.data)
   def test_fortune_2(self):
       with requests_mock.mock() as m:
           m.get('http://service2:5001/letter1', text='A')
           m.get('http://service3:5002/letter2', text='Y')
           response = self.client.get(url_for('fortune'))
           self.assertIn(b'AY', response.data)
       
   def test_fortune_3(self): 
       with requests_mock.mock() as m:
           m.get('http://service2:5001/letter1', text='B')
           m.get('http://service3:5002/letter2', text='X')
           response = self.client.get(url_for('fortune'))
           self.assertIn(b'BX', response.data)

   def test_fortune_4(self):
       with requests_mock.mock() as m:
           m.get('http://service2:5001/letter1', text='B')
           m.get('http://service3:5002/letter2', text='Y')
           response = self.client.get(url_for('fortune'))
           self.assertIn(b'BY', response.data)



