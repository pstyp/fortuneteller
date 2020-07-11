#!/bin/bash


sudo -E docker-compose build
sudo -E docker-compose push




scp docker-compose.yaml jenkins@project2:/home/jenkins/

ssh jenkins@project2 << EOF
export DATABASE=${DATABASE}
export PASSWORD=${PASSWORD}
docker stack deploy --compose-file docker-compose.yaml project

docker exec \$(docker ps -q -f name=project_service1) python3 create.py
EOF
