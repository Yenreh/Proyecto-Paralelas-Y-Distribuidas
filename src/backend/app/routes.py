from datetime import datetime

from flask import Blueprint, request, jsonify
from helpers import requestResponse

from models import db, Project, Task

app = Blueprint('main', __name__)


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
    new_project = Project(
        name=data['name'],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created'}), 201


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
    new_task = Task(
        project_id=data['project_id'],
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
            task.project_id = data['project_id']
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
