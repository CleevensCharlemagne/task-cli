def add_task(title, storage):
    task_id = storage.add(title)
    print(f"Task added successfully (ID: {task_id})")


def mark_in_progress(task_id, storage):
    storage.update_status(task_id, "in-progress")
    print(f"Task {task_id} marked as in progress")


def mark_done(task_id, storage):
    storage.update_status(task_id, "done")
    print(f"Task {task_id} marked as done")


def update(task_id, new_title, storage):
    success = storage.update_title(task_id, new_title)
    if success:
        print(f"Task updated successfully (ID: {task_id})")
    else:
        print("Task not found")


def delete(task_id, storage):
    success = storage.delete(task_id)
    if success:
        print(f"Task deleted successfully (ID: {task_id})")
    else:
        print("Task not found")


def show(storage, status=None):
    tasks = storage.get_all()

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        if status is None or task["status"] == status:
            print(f'ID: {task["id"]} - {task["title"]} [{task["status"]}]')