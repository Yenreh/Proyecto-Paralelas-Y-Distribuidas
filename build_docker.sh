#!/bin/bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
docker build -t backend:latest ./backend
docker tag backend:latest localhost:5000/backend:latest
docker push localhost:5000/backend:latest
docker build -t frontend:latest ./frontend
docker tag backend:latest localhost:5000/frontend:latest
docker push localhost:5000/frontend:latest
docker build -t database:latest ./database
docker tag backend:latest localhost:5000/database:latest
docker push localhost:5000/database:latest
