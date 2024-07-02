#!/bin/bash
docker stack rm backend_stack
docker stack rm frontend_stack
docker stack rm database_stack
sleep 5
docker rmi backend_image:latest
docker rmi frontend_image:latest
docker rmi database_image:latest
