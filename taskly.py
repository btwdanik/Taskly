import os
import argparse

from dotenv import load_dotenv
from task_repo import TaskRepo

load_dotenv()

name_storage = os.getenv("NAME_STORAGE")
taskly = TaskRepo(name_file=name_storage)

parser = argparse.ArgumentParser(description="Taskly")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add", help="Добавить задачу")
add_parser.add_argument("description", type=str)

update_parser = subparsers.add_parser("update", help="Обновить задачу")
update_parser.add_argument("id", type=int)
update_parser.add_argument("description", type=str)

delete_parser = subparsers.add_parser("delete", help="Удалить задачу")
delete_parser.add_argument("id", type=int)

done_parser = subparsers.add_parser("mark-done", help="Пометить задачу как выполненную")
done_parser.add_argument("id", type=int)

not_done_parser = subparsers.add_parser("mark-not-done", help="Пометить задачу как не выполненную")
not_done_parser.add_argument("id", type=int)

progress_parser = subparsers.add_parser("mark-in-progress", help="Пометить задачу как выполняемую")
progress_parser.add_argument("id", type=int)

list_parser = subparsers.add_parser("list", help="Показать все задачи")
list_parser.add_argument(
    "--status",
    choices=["done", "todo", "in-progress"],
    help="Фильтр по статусу"
)


def main():
    payload = parser.parse_args().__dict__
    if payload["command"] == "add":
        taskly.task_add(payload["description"])
    elif payload["command"] == "update":
        taskly.task_update(payload["id"], payload["description"])
    elif payload["command"] == "delete":
        taskly.task_delete(payload["id"])

    elif payload["command"] == "mark-done":
        taskly.task_mark("Done", payload["id"])
    elif payload["command"] == "mark-not-done":
        taskly.task_mark("Not done", payload["id"])
    elif payload["command"] == "mark-in-progress":
        taskly.task_mark("In progress", payload["id"])

    elif payload["command"] == "list" and payload["status"] == "done":
        taskly.task_list_done()
    elif payload["command"] == "list" and payload["status"] == "todo":
        taskly.task_list_not_done()
    elif payload["command"] == "list" and payload["status"] == "in-progress":
        taskly.task_list_in_progress()
    elif payload["command"] == "list":
        taskly.task_list()

if __name__ == "__main__":
    main()