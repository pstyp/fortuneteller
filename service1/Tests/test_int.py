import unittest
from unittest.mock import patch
import time
from flask import url_for
from urllib.request import urlopen
import requests_mock
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Fortune 




class TestBase(LiveServerTestCase):

     def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        return app



     def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/jenkins/chromedriver", options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()


     def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")        

     def test_server_is_up_and_running(self):
         response=urlopen("http://service2:5001")
         response=urlopen("http://service3:5002")
         response=urlopen("http://service4:5003")
         response = urlopen("http://localhost:5000")
         self.assertEqual(response.code, 200) 



class TestButton(TestBase):

    def test_button(self):
        self.driver.find_element_by_xpath('/html/body/div/form/button').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
