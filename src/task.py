from datetime import datetime

class Task:
    def __init__(self, name: str):
        self.name = name
        self.status = "Pending"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        # Chuyển task thành dict để lưu vào JSON
        return {
            "name": self.name,
            "status": self.status,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        # Tạo task từ dict (khi đọc từ JSON)
        task = cls(data["name"])
        task.status = data["status"]
        task.created_at = data["created_at"]
        return task
    
    def __str__(self):
        return f"{self.name} [{self.status}] (Created: {self.created_at})"