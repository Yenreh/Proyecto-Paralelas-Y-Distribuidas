from flask import jsonify
import json
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


def to_dict(model, db):
    """
    Convert a SQLAlchemy model to a dictionary.
    """
    if isinstance(model, list):
        return [to_dict(item) for item in model]
    elif isinstance(model, db.Model):
        return {c.name: getattr(model, c.name) for c in model.__table__.columns}
    else:
        raise TypeError("Invalid model type")


def requestResponse(data):
    if data:
        return jsonify({"data": data}), 200
    if data is None or data == []:
        return jsonify({'data': data}), 200
    return jsonify({'data': None, "message": "Data not Found"}), 404
