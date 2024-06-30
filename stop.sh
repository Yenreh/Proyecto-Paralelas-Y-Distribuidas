#!/bin/bash

# Navigate to src directory
cd src/k8s

# Stop Minikube
./minikube stop && ./minikube delete
