#!/bin/bashS
docker swarm init --advertise-addr  192.168.1.133
docker network create -d overlay --attachable --scope=swarm somenetwork