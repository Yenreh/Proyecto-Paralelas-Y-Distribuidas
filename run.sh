#!/bin/bash
# Navigate to src directory
cd src/swarm
docker swarm init --advertise-addr  192.168.1.133
docker stack deploy -c backend-deployment.yaml backend_stack
docker stack deploy -c frontend-deployment.yaml frontend_stack
docker stack deploy -c database-deployment.yaml database_stack