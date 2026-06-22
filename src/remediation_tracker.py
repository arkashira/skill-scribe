import json
from dataclasses import dataclass
from typing import List

@dataclass
class RemediationTask:
    id: int
    name: str
    completion_status: bool = False

class RemediationTracker:
    def __init__(self):
        self.tasks = []
        self.notifications = []

    def add_task(self, task: RemediationTask):
        self.tasks.append(task)

    def update_task_status(self, task_id: int, completion_status: bool):
        for task in self.tasks:
            if task.id == task_id:
                task.completion_status = completion_status
                if completion_status:
                    self.notifications.append(f"Task {task.name} completed")

    def get_progress(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completion_status)
        return completed_tasks / total_tasks if total_tasks > 0 else 0

    def get_notifications(self):
        return self.notifications

    def save_to_database(self):
        # In-memory database stand-in
        return json.dumps([task.__dict__ for task in self.tasks])

    def load_from_database(self, data: str):
        # In-memory database stand-in
        self.tasks = [RemediationTask(**task) for task in json.loads(data)]
