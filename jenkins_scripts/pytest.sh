#!/bin/bash

sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
pip3 install pytest -y

pwd
cd ..


python3 -m pytest --cov ./service1/application


python3 -m pytest --cov ./service2/application


python3 -m pytest --cov ./service3/application


python3 -m pytest --cov ./service4/application

