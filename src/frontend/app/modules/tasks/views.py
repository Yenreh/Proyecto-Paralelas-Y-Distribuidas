from flask import Blueprint, render_template, request, redirect, url_for
from general_config import get_general_context
app = Blueprint('tasks', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Tasks'

    return render_template(
        'tasks.html',
        **context
    )

