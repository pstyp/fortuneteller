#!/bin/bash


sudo -E docker-compose build
sudo -E docker-compose push




scp docker-compose.yaml jenkins@project2:/home/jenkins/

ssh jenkins@project2 << EOF
export DATABASE=${DATABASE}
export PASSWORD=${PASSWORD}
sudo -E docker stack deploy --compose-file docker-compose.yaml project
sleep 5
sudo -E docker exec \$(docker ps -q -f name=project_service1 | head -n 1) python3 create.py
EOF
