#!/bin/bash

sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install pytest

cd /home/jenkins/fortuneteller/service1

python3 -m pytest --cov ./application

cd /home/jenkins/fortuneteller/service2

python3 -m pytest --cov ./application

cd /home/jenkins/fortuneteller/service3

python3 -m pytest --cov ./application

cd /home/jenkins/fortuneteller/service4

python3 -m pytest --cov ./application

