#!/bin/bash

# Ejecutar pruebas de Locust para backend
locust -f backend.py --headless -u 100 -r 2 --csv=results/locust_backend_stats --stop-timeout 300

# Ejecutar pruebas de Locust para frontend
locust -f frontend.py --headless -u 100 -r 2 --csv=results/locust_frontend_stats --stop-timeout 300
