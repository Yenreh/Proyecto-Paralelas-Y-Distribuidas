#!/bin/bash
# Navigate to src directory
cd src/k8s
export PATH=$(pwd):${PATH}

# Start Minikube
minikube start --cpus 6 --memory 8192

# Build Docker images into Minikube
minikube image build -t backend:latest ../backend
minikube image build -t frontend:latest ../frontend
minikube image build -t database:latest ../database

# Apply Kubernetes deployment files
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f database-deployment.yaml