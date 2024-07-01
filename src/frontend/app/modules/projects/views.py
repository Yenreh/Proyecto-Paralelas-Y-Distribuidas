from flask import Blueprint, render_template, request, redirect, url_for
from general_config import get_general_context
app = Blueprint('projects', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Projects'

    return render_template(
        'projects.html',
        **context
    )

