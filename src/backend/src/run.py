from flask import Flask
from models import db
import routes
from flask_cors import CORS
from general_config import get_db_config

app = Flask(__name__)
CORS(app)


class Config:
    db_config = get_db_config()
    SQLALCHEMY_DATABASE_URI = f"mysql://{db_config['username']}:{db_config['password']}@{db_config['hostname']}:{db_config['port']}/{db_config['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    app.register_blueprint(routes.app, url_prefix='/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


