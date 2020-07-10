#!/bin/bash

pwd

cd .. 
/home/jenkins/.local/bin/ansible-playbook -v -i inventory playbook.yaml


