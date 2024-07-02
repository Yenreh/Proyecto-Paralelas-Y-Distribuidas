#!/bin/bash
# Navigate to src directory
cd src/k8s

docker stack deploy -c docker_swarm/backend-deployment.yaml backend_stack
docker stack deploy -c docker_swarm/frontend-deployment.yaml frontend_stack
docker stack deploy -c docker_swarm/database-deployment.yaml database_stack