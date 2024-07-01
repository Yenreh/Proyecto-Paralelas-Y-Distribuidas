import json
import requests
import os
from pathlib import Path

def loadJSON(file_path: str):
    if Path(file_path).is_file() is False:
        raise FileNotFoundError(f"File not found: {file_path}")
    return json.loads(readFile(file_path))


def readFile(file_path: str):
    try:
        with Path(file_path).open() as data:
            return data.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def fetch_data_from_api(endpoint):
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()  # Suponiendo que la API devuelve datos en formato JSON
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
        return None
