from flask import Blueprint, render_template
from general_config import get_general_context, get_api_endpoint
from helper import process_table_data

app = Blueprint('tasks', __name__, template_folder='templates', static_folder='static')

VERBOSE_COLS = {
    'name': 'Name',
    'created_at': 'Created At',
    'updated_at': 'Updated At',
    'id': 'ID',
    'project_id': 'Project ID'
}


@app.route('/')
def index():
    context = get_general_context()
    context['model_data_name'] = 'Tasks'
    endpoint = get_api_endpoint()+"/tasks"
    data = process_table_data(endpoint, VERBOSE_COLS)
    context['show_table'] = True
    context['records'] = data['records']
    context['col_names'] = data['col_names']
    context['form_data'] = data['form_data']
    context['dropdown_fields'] = [{
        'name': 'project_id',
        'endpoint': get_api_endpoint() + '/projects'
    }]
    context['endpoint_url'] = endpoint
    context['show_details'] = False
    return render_template(
        'tasks.html',
        **context
    )

