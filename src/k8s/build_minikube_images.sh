#!/bin/bash
minikube image build -t backend:latest ../backend
minikube image build -t frontend:latest ../frontend
minikube image build -t database:latest ../database
