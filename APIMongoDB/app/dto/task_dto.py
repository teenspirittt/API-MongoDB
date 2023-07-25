class TaskDTO:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    @classmethod
    def from_model(cls, task_model):
        return cls(task_model.id, task_model.title, task_model.description)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }


