import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def _read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def get_all(self):
        return self._read()

    def add(self, title):
        data = self._read()
        task_id = len(data) + 1

        data.append({
            "id": task_id,
            "title": title,
            "status": "todo"
        })

        self._write(data)
        return task_id

    def update_status(self, task_id, status):
        data = self._read()

        for task in data:
            if task["id"] == task_id:
                task["status"] = status
                self._write(data)
                return True

        return False

    def update_title(self, task_id, new_title):
        data = self._read()

        for task in data:
            if task["id"] == task_id:
                task["title"] = new_title
                self._write(data)
                return True

        return False

    def delete(self, task_id):
        data = self._read()

        new_data = [task for task in data if task["id"] != task_id]

        if len(data) == len(new_data):
            return False

        # 🔥 Reassign IDs (list behavior)
        for i, task in enumerate(new_data, start=1):
            task["id"] = i

        self._write(new_data)
        return True