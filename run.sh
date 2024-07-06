#!/bin/bash
# Navigate to src directory
cd src/swarm
docker stack deploy -c database-deployment.yaml database_stack
docker stack deploy -c backend-deployment.yaml backend_stack
sleep 10
docker stack deploy -c frontend-deployment.yaml frontend_stack