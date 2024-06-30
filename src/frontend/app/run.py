from flask import Flask, render_template
import modules.projects.views as projects_views
import modules.tasks.views as tasks_views

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'SECRET_KEY'
app.register_blueprint(projects_views.app, url_prefix='/projects')
app.register_blueprint(tasks_views.app, url_prefix='/tasks')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5555, debug=True)

