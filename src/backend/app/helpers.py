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