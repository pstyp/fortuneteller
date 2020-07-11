#!/bin/bash


docker-compose build
docker-compose push




scp docker-compose.yaml jenkins@project2:/home/jenkins/

ssh jenkins@project2 << EOF
docker stack deploy --compose-file docker-compose.yaml project
sleep 5
docker exec \$(docker ps -q -f name=project_service1) python3 create.py
EOF
