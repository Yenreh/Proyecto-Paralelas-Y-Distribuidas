from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('tasks', __name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('tasks.html')

