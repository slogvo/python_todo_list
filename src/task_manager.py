from src.task import Task
from src.storage import Storage

class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()
    
    def add_task(self, name: str):
        if not name.strip():
            raise ValueError("Task name cannot be empty!")
        task = Task(name)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
    
    def remove_task(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise ValueError("Invalid task index!")
        self.tasks.pop(index)
        self.storage.save_tasks(self.tasks)
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")