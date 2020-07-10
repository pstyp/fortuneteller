#!/bin/bash

source /home/jenkins/env_var.sh

sudo apt-get install python3 -y
sudo apt-get install python3-pip python3-venv -y

python3 -m venv venv 
. venv/bin/activate


pip3 install pytest pytest-cov 
pwd

pip3 install -r ./service1/requirements.txt

python3 -m pytest --cov ./service1/application


python3 -m pytest --cov ./service2/application


python3 -m pytest --cov ./service3/application


python3 -m pytest --cov ./service4/application

