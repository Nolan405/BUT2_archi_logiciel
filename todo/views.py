from flask import jsonify, abort, make_response, request, url_for
from .app import app
from .models import tasks


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    public_tasks = []
    for task in tasks:
        public_tasks.append(make_public_task(task))
    return jsonify({'tasks': public_tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify({'task': task})
    return {'error': 'Not found'}, 404

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return {'error': 'Bad request'}, 400
    if tasks == []:
        new_id = 1
    else:
        new_id = tasks[-1]['id'] + 1    
    task = {
        'id': new_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': request.json.get('done', False),
    }
    tasks.append(task)
    return jsonify({'task': make_public_task(task)}), 201
