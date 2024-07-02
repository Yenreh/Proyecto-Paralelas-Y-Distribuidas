#!/bin/bash

# Ejecutar pruebas de Locust para backend
locust -f backend.py --headless -u 10 -r 1 --csv=results/locust_backend_stats --stop-timeout 60

# Ejecutar pruebas de Locust para frontend
#locust -f frontend.py --headless -u 10 -r 1 --csv=results/locust_frontend_stats
