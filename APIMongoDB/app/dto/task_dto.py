class TaskDTO:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    @classmethod
    def from_model(cls, task_model):
        return cls(str(task_model.id), task_model.title, task_model.description)

    def to_dict(self):
        return {
            'id': str(self.id), 
            'title': self.title,
            'description': self.description
        }

    @staticmethod
    def from_dict(task_dict):
        task_id = task_dict.get('_id')
        title = task_dict.get('title')
        description = task_dict.get('description')
        return TaskDTO(task_id, title, description)