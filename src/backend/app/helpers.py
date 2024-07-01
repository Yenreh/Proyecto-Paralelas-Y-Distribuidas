from flask import jsonify


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
    print(data)
    if data:
        return jsonify({"data": data}), 200
    if data is None or data == []:
        return jsonify({'data': data}), 200
    return jsonify({'data': None}), 404