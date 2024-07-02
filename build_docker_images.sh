#!/bin/bash
cd src
docker build -t backend_image:latest ./backend
docker build -t frontend_image:latest ./frontend
docker build -t database_image:latest ./database