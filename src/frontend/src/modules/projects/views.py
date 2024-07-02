from flask import Blueprint, render_template
from general_config import get_general_context, get_api_endpoint, get_api_external_endpoint
from helper import process_table_data

app = Blueprint('projects', __name__, template_folder='templates', static_folder='static')

VERBOSE_COLS = {
    'name': 'Name',
    'created_at': 'Created At',
    'updated_at': 'Updated At',
    'id': 'ID'
}


@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Projects'
    endpoint = get_api_endpoint()+"/projects"
    data = process_table_data(endpoint, VERBOSE_COLS)
    context['show_table'] = True
    context['records'] = data['records']
    context['col_names'] = data['col_names']
    context['form_data'] = data['form_data']
    context['endpoint_url'] = get_api_external_endpoint() + '/projects'
    context['show_details'] = True
    print(context)
    return render_template(
        'projects.html',
        **context
    )

