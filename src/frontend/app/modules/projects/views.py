from flask import Blueprint, render_template, request, redirect, url_for
from general_config import get_general_context, get_api_endpoint
from helper import fetch_data_from_api
app = Blueprint('projects', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Projects'
    endpoint = get_api_endpoint()+"/projects"
    data = fetch_data_from_api(endpoint)
    print(type(data))

    # if data is not None:
    #     context['model_data'] = data

    return render_template(
        'projects.html',
        **context
    )

