from flask import Blueprint
from controllers.task_controller import TaskController


task_bp = Blueprint('task_bp', __name__)

task_controller = TaskController()


@task_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = task_controller.get_all_tasks()
    return tasks


@task_bp.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = task_controller.get_task(task_id)
    return task


@task_bp.route('/tasks', methods=['POST'])
def create_task():
    return task_controller.create_task()


@task_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    return task_controller.update_task(task_id)


@task_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return task_controller.delete_task(task_id)