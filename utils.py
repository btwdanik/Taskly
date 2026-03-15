import os

from rich.table import Table

def get_data_path():
    data_dir = os.path.expanduser("~/.local/share/taskly")
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "tasks.json")

def console_table(table: Table, task):
    task_status = "[green]Done[/green]" if task["status"] == "Done" else (
        "[yellow]In progress[/yellow]" if task["status"] == "In progress" else
            "[red]Not done[/red]")

    task_description = f"[strike]{task["description"]}[/strike]" if (
        task["status"] == "Done") else task["description"]

    table.add_row(
        str(task["id"]),
        task_description,
        task_status,
        str(task["createdAt"]),
        str(task["updatedAt"]),
    )

    return table

def console_table_delete(table: Table, task):
    task_status = "[green]Done[/green]" if task["status"] == "Done" else (
        "[yellow]In progress[/yellow]" if task["status"] == "In progress" else
            "[red]Not done[/red]")

    table.add_row(
        f"[strike]{task["id"]}[/strike]",
        f"[strike]{task["description"]}[/strike]",
        f"[strike]{task_status}[/strike]",
        f"[strike]{task["createdAt"]}[/strike]",
        f"[strike]{task["updatedAt"]}[/strike]",
    )

    return table