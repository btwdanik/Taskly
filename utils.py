from rich.table import Table

def console_table(table: Table, task):
    task_status = "[green]Done[/green]" if task["status"] == "Done" else (
        "[yellow]In progress[/yellow]" if task["status"] == "In progress" else
            "[red]Not done[/red]")

    task_description = f"[strike dim]{task["description"]}[/strike dim]" if (
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
        f"[strike dim]{task["id"]}[/strike dim]",
        f"[strike dim]{task["description"]}[/strike dim]",
        f"[strike dim]{task_status}[/strike dim]",
        f"[strike dim]{task["createdAt"]}[/strike dim]",
        f"[strike dim]{task["updatedAt"]}[/strike dim]",
    )

    return table