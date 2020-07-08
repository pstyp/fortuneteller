import unittest
  
from flask import url_for, request
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
        config_name='testing'
        return app



class TestViews(TestBase):
    def test_url2(self):
        response=self.client.get(url_for('letter2'))
        self.assertEqual(response.status_code, 200)
