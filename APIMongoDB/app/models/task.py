class Task:
    def __init__(self, task_id, title, description, variant):
        self.id = task_id
        self.title = title
        self.description = description

    @staticmethod
    def from_dict(task_dict):
        return Task(task_dict['id'], task_dict['title'], task_dict['description'])

    def to_dict(self):
        return self.__dict__

    def update(self, task_data):
        if 'title' in task_data:
            self.title = task_data['title']
        if 'description' in task_data:
            self.description = task_data['description']
