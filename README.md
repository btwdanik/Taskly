# Taskly: CLI Task Tracker / TODO

## 📖 Description

**Taskly** is a lightweight command-line interface (CLI) application for managing tasks from the terminal.  
It lets you **add, update, delete, list, and track tasks** without leaving the command line.

The project is built with Python and stores all task data in a JSON file, making it simple, transparent, and easy to extend.

---

## ✨ Features

- **Add a Task** → Create a new task with a description. Each task gets a unique ID and the default status `Todo`.
- **Update a Task** → Change the description of an existing task.
- **Mark as In Progress** → Update a task status to `In Progress`.
- **Mark as Done** → Update a task status to `Done`.
- **Delete a Task** → Remove a task by its ID.
- **List Tasks** → Show all tasks or filter them by status:
  - `todo`
  - `in-progress`
  - `done`

---

## 🗂 Project Structure

- **taskly.py** → Main CLI entry point
  - `main()` → Parses CLI arguments and dispatches commands.

- **task_repo.py** → Task storage and business logic
  - `task_add(...)` → Adds a new task
  - `task_update(...)` → Updates task description
  - `task_delete(...)` → Deletes a task
  - `task_mark(...)` → Changes task status
  - `task_list(...)` → Returns tasks, optionally filtered
  - Handles reading/writing tasks to JSON

- **dependency.py** → Auxiliary utilities and shared helpers


---

## ⚡ Installation

Clone the repository:

```bash
pip install https://github.com/btwdanik/Taskly.git
```

## 🚀 Usage

```bash
$ taskly add [-h] description

$ taskly update [-h] id description

$ taskly delete [-h] id

$ taskly mark-done [-h] id

$ taskly mark-in-progress [-h] id

$ taskly list [-h] [--status {done,todo,in-progress}]
```