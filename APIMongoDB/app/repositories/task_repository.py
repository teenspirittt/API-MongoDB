from pymongo import MongoClient
from bson.objectid import ObjectId
from dto.task_dto import TaskDTO
from models.task import Task

class TaskRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://mongo:27017")
        self.db = self.client["mydatabase"]
        self.tasks_collection = self.db["tasks"]

    def get_all_tasks(self):
        tasks = list(self.tasks_collection.find())
        return [TaskDTO.from_dict(task) for task in tasks]

    def get_task_by_id(self, task_id):
        task = self.tasks_collection.find_one({"_id": ObjectId(task_id)})
        if task:
            return TaskDTO.from_dict(task)
        return None

    def create_task(self, task_data):
        result = self.tasks_collection.insert_one(task_data)
        return str(result.inserted_id)

    def update_task(self, task_id, task_data):
        try:
            result = self.tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": task_data})
            if result.matched_count > 0:
                if result.modified_count > 0:
                    return True
                return False
            return None
        except Exception as e:
            return False

    def delete_task(self, task_id):
        result = self.tasks_collection.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count > 0