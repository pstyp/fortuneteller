#!/bin/bash

source /home/jenkins/env_var.sh

sudo apt-get install python3 -y
sudo apt-get install python3-pip python3-venv -y

python3 -m venv venv 
. venv/bin/activate


pip3 install pytest pytest-cov
pip3 install requests_mock
pwd

pip3 install -r ./service1/requirements.txt

cd service1 
python3 -m pytest --cov ./application
cd ..

cd service2
python3 -m pytest --cov ./application
cd ..
cd service3
python3 -m pytest --cov ./application
cd ..

cd service4
python3 -m pytest --cov ./application
cd ..
