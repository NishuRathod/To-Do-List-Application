class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "DONE" if self.completed else "PENDING"
        return f"[{self.task_id}] {self.description} - {status}"
