#!/bin/bash
docker rmi backend_image:latest
docker rmi frontend_image:latest
docker rmi database_image:latest