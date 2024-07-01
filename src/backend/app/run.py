from flask import Flask, render_template
from models import db
import routes

CONFIG_PATH = 'config/config.json'
app = Flask(__name__)


class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:password@database-deployment:3306/administrator_db'
    SQLALCHEMY_DATABASE_URI = 'mysql://yenreh:3289@127.0.0.1:3306/administrator_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    app.register_blueprint(routes.app, url_prefix='/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556, debug=True)


