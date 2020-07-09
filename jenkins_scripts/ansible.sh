#!/bin/bash

sudo apt-get update
sudo apt-get install python3 -y
sudo apt-get install python3-pip
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
ansible --version

ansible-playbook -v -i inventory playbook.yaml
