from flask import Flask, render_template
import routes

app = Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@database-deployment:3306/administrator_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
with app.app_context():
    app.register_blueprint(routes.app, url_prefix='/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)


