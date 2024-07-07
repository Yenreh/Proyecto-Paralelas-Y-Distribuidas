from datetime import datetime
from flask import Blueprint, request, jsonify
from helper import requestResponse, saveLog
from models import db, Project, Task
from general_config import get_log_path

app = Blueprint('main', __name__)
log_path = get_log_path()


@app.after_request
def log_action_result(response):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - {request.method} {request.path} - Status: {response.status_code}"
    saveLog(log_message=log_message, file_path=log_path)
    return response


@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return requestResponse(projects)


@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get(id)
    return requestResponse(project)


@app.route('/projects/create', methods=['POST'])
def create_project():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'No project name provided'}), 400
    new_project = Project(
        name=data['name'],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created'}), 201


@app.route('/projects/<int:id>/tasks', methods=['GET'])
def get_project_tasks(id):
    tasks = Task.query.filter_by(project_id=id).all()
    return requestResponse(tasks)


@app.route('/projects/update/<int:id>', methods=['PUT'])
def update_project(id):
    project = Project.query.get(id)
    if project:
        data = request.get_json()
        project.name = data['name']
        project.updated_at = datetime.now()
        db.session.commit()
        return jsonify({'message': 'Project updated'}), 200
    return jsonify({'message': 'Project not found'}), 404


@app.route('/projects/delete/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get(id)
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted'}), 200
    return jsonify({'message': 'Project not found'}), 404

# Similar endpoints for tasks


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return requestResponse(tasks)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return requestResponse(task)


@app.route('/tasks/create', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'name' not in data or 'project_id' not in data:
        return jsonify({'message': 'Missing task name or project id'}), 400
    try:
        project_id = int(data['project_id'])
    except ValueError:
        return jsonify({'message': 'Project id must be an integer'}), 400
    new_task = Task(
        project_id=project_id,
        name=data['name'],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201


@app.route('/tasks/update/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if task:
        data = request.get_json()
        if 'project_id' in data:
            try:
                data['project_id'] = int(data['project_id'])
            except ValueError:
                return jsonify({'message': 'Project id must be an integer'}), 400
        task.name = data['name']
        task.updated_at = datetime.now()
        db.session.commit()
        return jsonify({'message': 'Task updated'}), 200
    return jsonify({'message': 'Task not found'}), 404


@app.route('/tasks/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'message': 'Task not found'}), 404
