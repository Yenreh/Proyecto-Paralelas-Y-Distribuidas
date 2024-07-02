from flask import Flask, redirect
import modules.projects.views as projects_views
import modules.tasks.views as tasks_views
from general_config import get_general_context, get_app_secret
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
app.secret_key = get_app_secret()
app.register_blueprint(projects_views.app, url_prefix='/projects')
app.register_blueprint(tasks_views.app, url_prefix='/tasks')


@app.route('/')
def index():
    # context = get_general_context()
    return redirect('/projects')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)

