#!/bin/bash


source /home/jenkins/env_var.sh


sudo docker-compose build
sudo docker-compose push

scp docker-compose.yaml jenkins@project2:/home/jenkins/

ssh jenkins@project2 << EOF
sudo docker stack deploy --compose-file docker-compose.yaml project
sleep 5
sudo docker exec \$(docker ps -q -f name=project_service1) python3 create.py
EOF
