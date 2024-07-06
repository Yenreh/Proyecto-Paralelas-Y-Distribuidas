#!/bin/bash

# Ejecutar pruebas de Locust para backend
locust -f  backend.py --headless -u 100 -r 2 -t 5m --csv=results/locust_backend_stats

# Ejecutar pruebas de Locust para frontend
locust -f frontend.py --headless -u 100 -r 2 -t 5m --csv=results/locust_frontend_stats
