#!/bin/bash

source /home/jenkins/env_var.sh 

docker-compose build
docker-compose push

ssh pstyp94@project2 << EOF

docker stack deploy --compose-file docker-compose.yaml project

docker exec $(docker ps -q -f name=project_service1) python3 create.py

EOF
