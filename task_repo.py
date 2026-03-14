import json
from datetime import datetime

from rich.console import Console
from rich.table import Table

from dependency import Schema

class TaskRepo:
    def __init__(self, name_file):
        self.name_file = name_file
        self.console = Console()
        self.table = Table(title="My tasks")
        self.table.add_column("Id", justify="right", style="cyan")
        self.table.add_column("Description", style="white")
        self.table.add_column("Status")
        self.table.add_column("Created at", style="magenta")
        self.table.add_column("Updated at", style="magenta")

    def task_add(self, description) -> None:
        with open(self.name_file, "r+", encoding="utf-8") as f:
            data = json.load(f)
            if data:
                num_task = data[-1]["id"] + 1
            else:
                num_task = 1
            schema = Schema(
                id=num_task,
                description=description,
            )
            data.append(schema.to_dict())
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            self.console.print(f"[green]Task added successfully (ID: [/green][cyan]{num_task}[/cyan][green])[/green]")
            return None

    def task_delete(self, num_task) -> None:
        with open(file=self.name_file, mode='r+') as f:
            data = json.load(f)
            if data:
                new_data = [task for task in data if task["id"] != num_task]
                f.seek(0)
                json.dump(new_data, f, ensure_ascii=False, indent=4)
                f.truncate()
                if len(new_data) != len(data):
                    self.console.print(f"[green]Task deleted successfully (ID: [/green][cyan]{num_task}[/cyan][green])[/green]")
                    return None
            self.console.print("[red]The task was not found[/red]")
            return None

    def task_update(self, num_task, description) -> None:
        with open(file=self.name_file, mode='r+') as f:
            data = json.load(f)
            if data:
                flag = False
                for task in data:
                    if task["id"] == num_task:
                        task["description"] = description
                        task["updatedAt"] = datetime.now().replace(microsecond=0).isoformat()
                        flag = True
                        break
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
                if flag:
                    self.console.print(f"[green]Task updated successfully (ID: [/green][cyan]{num_task}[/cyan][green])[/green]")
                    return None
            self.console.print("[red]The task was not found[/red]")
            return None

    def task_mark(self, mark, num_task) -> None:
        with open(file=self.name_file, mode='r+') as f:
            data = json.load(f)
            if data:
                flag = False
                for task in data:
                    if task["id"] == num_task:
                        task["status"] = mark
                        task["updatedAt"] = datetime.now().replace(microsecond=0).isoformat()
                        flag = True
                        break
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
                if flag:
                    self.console.print(f"[green]Task status updated successfully (ID: [/green][cyan]{num_task}[/cyan][green])[/green]")
                    return None
            self.console.print("[red]The task was not found[/red]")
            return None

    def task_list(self) -> None:
        with open(file=self.name_file, mode='r') as f:
            for task in json.load(f):
                print(task)
                status = "[green]Done[/green]" if task["status"] == "Done" else ("[yellow]In progress[/yellow]" if task["status"] == "In progress" else "[red]Not done[/red]")
                self.table.add_row(
                    str(task["id"]),
                    task["description"],
                    status,
                    task["createdAt"],
                    task["updatedAt"]
                )
            self.console.print(self.table)
            return None

    def task_list_done(self) -> None:
        with open(file=self.name_file, mode='r') as f:
            for task in json.load(f):
                if task["status"] == "Done":
                    self.table.add_row(
                        str(task["id"]),
                        task["description"],
                        "[green]Done[/green]",
                        task["createdAt"],
                        task["updatedAt"])
            self.console.print(self.table)
            return None

    def task_list_not_done(self) -> None:
        with open(file=self.name_file, mode='r') as f:
            for task in json.load(f):
                if task["status"] == "Not done":
                    self.table.add_row(
                        str(task["id"]),
                        task["description"],
                        "[red]Not done[/red]",
                        task["createdAt"],
                        task["updatedAt"]
                    )
            self.console.print(self.table)
            return None

    def task_list_in_progress(self) -> None:
        with open(file=self.name_file, mode='r') as f:
            for task in json.load(f):
                if task["status"] == "In progress":
                    self.table.add_row(
                        str(task["id"]),
                        task["description"],
                        "[yellow]In progress[/yellow]",
                        task["createdAt"],
                        task["updatedAt"]
                    )
            self.console.print(self.table)
            return None