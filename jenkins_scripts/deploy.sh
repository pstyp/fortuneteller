#!/bin/bash

docker-compose build
docker-compose push

docker stack deploy --compose-file docker-compose.yaml project
docker exec -it  project_service1.1.xuz3enurztukckyy01p2iaio4 python3 create.py

