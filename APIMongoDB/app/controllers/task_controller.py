from flask import request, jsonify
from repositories.task_repository import TaskRepository
from dto.task_dto import TaskDTO
import bson
from bson import errors, ObjectId

class TaskController:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        tasks = self.task_repository.get_all_tasks()
        return jsonify([task.to_dict() for task in tasks])

    def get_task(self, task_id):
        try:
            task_id = ObjectId(task_id)
            task = self.task_repository.get_task_by_id(task_id)
            if task:
                return task.to_dict()
            return {"error": "Task not found."}, 404
        except errors.InvalidId as e:
            return {"error": "Invalid id format."}, 400

    def create_task(self):
        task_data = request.json
        try:
            inserted_id = self.task_repository.create_task(task_data)
            task = self.task_repository.get_task_by_id(inserted_id)
            return task.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 500

    def update_task(self, task_id):
        task_data = request.json
        try:
            task_id = ObjectId(task_id)
            update_result = self.task_repository.update_task(task_id, task_data)
            if update_result is None:
                return {"error": "Task not found."}, 404
            elif update_result:
                return {"message": "Task successfully updated."}, 200
            else:
                return {"error": "No changes made to the task."}, 400
        except bson.errors.InvalidId:
            return {"error": "Invalid id format."}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def delete_task(self, task_id):
        task_id = ObjectId(task_id)
        if self.task_repository.delete_task(task_id):
            return {"message": "Task successfully deleted."}, 200
        return {"error": "Task not found."}, 404