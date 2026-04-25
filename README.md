# Task CLI 📝

A simple command-line task manager built with Python.  
This project allows you to add, update, delete, and track tasks directly from the terminal.

---

## 🚀 Features

- Add new tasks
- Mark tasks as in-progress or done
- Update task titles
- Delete tasks
- List all tasks or filter by status
- Simple JSON-based storage (no database needed)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-cli.git
cd task-cli
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install the project in editable mode
```bash
pip install -e .
```

## ⚙️ Usage
### After installation, you can use the CLI globally:
```bash
task-cli add "Learn python"
```

## 📌 Commands
### ➕ Add a task
```bash
task-cli add "Task title"
```

### 🔄 Mark task as in progress
```bash
task-cli mark-done 1
```

### ✏️ Update a task
```bash
task-cli update 1 "New task title"
```

### ❌ Delete a task
```bash
task-cli delete 1
```

### 📋 List tasks
```bash
task-cli list
```
Filter by status:
```bash
task-cli list todo
task-cli list done
task-cli list in-progress
```

## 🧠 How it works
- Tasks are stored in a local JSON file
- Each task has:
  - id
  - title
  - status (todo, in-progress, done)
- IDs are automatically reassigned after deletion (list-style behavior)

## 🗂 Project Structure
```commandline
task-cli/
│
├── task_cli/
│   ├── __init__.py
│   ├── main.py
│   ├── commands.py
│   ├── dispatcher.py
│   └── storage.py
│
├── setup.py
└── README.md
```

## 🛠 Tech Stack
- Python 3
- JSON for storage
- setuptools for CLI packaging

## 📌 Future improvements
- Add timestamps (created_at, updated_at)
- Add search functionality
- Add priority levels
- Add SQLite database support
- Improve CLI output with colors

## 👨‍💻 Author

Built as a learning project to practice:
- Python CLI development
- File handling
- Project structuring
- Command routing design