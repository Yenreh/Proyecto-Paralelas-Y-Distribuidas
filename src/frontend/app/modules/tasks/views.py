from flask import Blueprint, render_template, request, redirect, url_for
from general_config import get_general_context, get_api_endpoint
from helper import fetch_data_from_api

app = Blueprint('tasks', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Tasks'
    endpoint = get_api_endpoint()+"/tasks"
    data = fetch_data_from_api(endpoint)
    records = []
    col_names = []
    if data:
        records = data['data']
        col_names = list(records[0].keys())
    context['show_table'] = True
    context['records'] = records
    context['col_names'] = col_names
    return render_template(
        'tasks.html',
        **context
    )

