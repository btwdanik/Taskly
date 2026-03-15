import json
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich import box

from dependency import Schema
from utils import console_table, console_table_delete

class TaskRepo:
    def __init__(self, name_file):
        self.name_file = name_file
        self.console = Console()
        self.table =  Table(
            title="✨ My Tasks",
            title_style="bold cyan",
            box=box.ROUNDED,
            border_style="bright_blue",
            header_style="bold cyan",
            show_lines=True,
            padding=(0, 2),
            expand=False,
        )
        self.table.add_column("Id", justify="right", style="cyan")
        self.table.add_column("Description", style="white")
        self.table.add_column("Status")
        self.table.add_column("Created at", style="magenta")
        self.table.add_column("Updated at", style="magenta")

    def task_add(self, description) -> None:
        try:
            with open(self.name_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        if data:
            num_task = str(max(int(k) for k in data.keys()) + 1)
        else:
            num_task = "1"
        schema = Schema(
            id=num_task,
            description=description,
        )
        data[num_task] = schema.to_dict()

        with open(file=self.name_file, mode='w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            console_table(self.table, schema.to_dict())
            self.console.print("\n", self.table, "\n")

    def task_delete(self, num_task) -> None:
        try:
            with open(self.name_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        if data:
            if data.get(num_task, False) != False:
                task = data[num_task]
                del data[num_task]
                with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    console_table_delete(self.table, task)
                    self.console.print("\n", self.table, "\n")
            else:
                self.console.print("[red]The task was not found[/red]")
        else:
            self.console.print("[red]The task was not found[/red]")

    def task_update(self, num_task, description) -> None:
        try:
            with open(self.name_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        if data:
            if data.get(num_task, False) != False:
                task = data[num_task]
                data[num_task]["description"] = description
                data[num_task]["updatedAt"] = datetime.now().replace(microsecond=0).isoformat()
                with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    console_table(self.table, task)
                    self.console.print("\n", self.table, "\n")
            else:
                self.console.print("[red]The task was not found[/red]")
        else:
            self.console.print("[red]The task was not found[/red]")

    def task_mark(self, mark, num_task) -> None:
        try:
            with open(self.name_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        if data:
            if data.get(num_task, False) != False:
                task = data[num_task]
                data[num_task]["status"] = mark
                data[num_task]["updatedAt"] = datetime.now().replace(microsecond=0).isoformat()
                with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    console_table(self.table, task)
                    self.console.print("\n", self.table, "\n")
            else:
                self.console.print("[red]The task was not found[/red]")
        else:
            self.console.print("[red]The task was not found[/red]")

    def task_list(self) -> None:
        try:
            with open(file=self.name_file, mode='r') as f:
                data = json.load(f)
                for task in data:
                    console_table(self.table, data[task])
                self.console.print("\n", self.table, "\n")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
            with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                self.console.print("\n", self.table, "\n")

    def task_list_done(self) -> None:
        try:
            with open(file=self.name_file, mode='r') as f:
                data = json.load(f)
                for task in data:
                    if data[task]["status"] == "Done":
                        console_table(self.table, data[task])
                self.console.print("\n", self.table, "\n")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
            with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                self.console.print("\n", self.table, "\n")

    def task_list_not_done(self) -> None:
        try:
            with open(file=self.name_file, mode='r') as f:
                data = json.load(f)
                for task in data:
                    if data[task]["status"] == "Not done":
                        console_table(self.table, data[task])
                self.console.print("\n", self.table, "\n")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
            with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                self.console.print("\n", self.table, "\n")

    def task_list_in_progress(self) -> None:
        try:
            with open(file=self.name_file, mode='r') as f:
                data = json.load(f)
                for task in data:
                    if data[task]["status"] == "In progress":
                        console_table(self.table, data[task])
                self.console.print("\n", self.table, "\n")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
            with open(file=self.name_file, mode='w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                self.console.print("\n", self.table, "\n")
