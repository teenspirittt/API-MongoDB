class TaskDTO:
    def __init__(self, task_id, title, description):
        self.id = str(task_id)  # Преобразуем ObjectId в строку
        self.title = title
        self.description = description

    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['_id'], task_dict['title'], task_dict['description'])

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
