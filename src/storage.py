import json
import os

from src.task import Task


class Storage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        # Tạo thư mục data nếu chưa có
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
