from app.task import Task

class TodoApp:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def add_task(self, description):
        task = Task(self.counter, description)
        self.tasks[self.counter] = task
        print("Task added.")
        self.counter += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks.values():
            print(task)

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completed()
            print("Task completed.")
        else:
            print("Invalid Task ID.")
