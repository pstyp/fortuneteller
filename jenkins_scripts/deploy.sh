#!/bin/bash

source /home/jenkins/env_var.sh 


sudo docker-compose build
sudo docker-compose push



ssh jenkins@project2 << EOF

sudo docker stack deploy --compose-file docker-compose.yaml project

sudo docker exec $(docker ps -q -f name=project_service1) python3 create.py

EOF
