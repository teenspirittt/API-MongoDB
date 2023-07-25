from flask import request
from repositories.task_repository import TaskRepository


class TaskController:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        tasks = self.task_repository.get_all_tasks()
        return tasks

    def get_task(self, task_id):
        task = self.task_repository.get_task_by_id(task_id)
        if task:
            return task
        return {"error": "Task not found."}, 404

    def create_task(self):
        task_data = request.json
        inserted_id = self.task_repository.create_task(task_data)
        return {"inserted_id": inserted_id}, 201

    def update_task(self, task_id):
        task_data = request.json
        update_result = self.task_repository.update_task(task_id, task_data)
        if update_result is None:
            return {"error": "Task not found."}, 404
        elif update_result:
            return {"message": "Task successfully updated."}, 200
        else:
            return {"error": "No changes made to the task."}, 400


    def delete_task(self, task_id):
        if self.task_repository.delete_task(task_id):
            return {"message": "Task successfully deleted."}, 200
        return {"error": "Task not found."}, 404
