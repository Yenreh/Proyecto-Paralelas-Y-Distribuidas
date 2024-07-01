import json
import requests
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


def process_table_data(endpoint, verbose_cols=None):
    if verbose_cols is None:
        verbose_cols = {}
    data = fetch_data_from_api(endpoint)
    records = []
    col_names = []
    form_data = {}
    if data:
        records = data['data']
        keys = list(records[0].keys())
        col_names = [{'name': verbose_cols[key], 'id': key} if key in verbose_cols.keys() else {'name': key, 'id': key} for key in keys]
        form_data = {key: "" for key in keys}
    return {"records": records, "col_names": col_names, "form_data": form_data}
