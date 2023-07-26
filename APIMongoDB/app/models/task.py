class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description

    @staticmethod
    def from_dict(task_dict):
        return Task(task_dict['_id'], task_dict['title'], task_dict['description'])

    def to_dict(self):
        return self.__dict__

    def update(self, task_dict):
        if 'title' in task_dict:
            self.title = task_dict['title']
        if 'description' in task_dict:
            self.description = task_dict['description']
