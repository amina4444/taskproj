from typing import Callable

import flet as ft


class Person:
    pass


def create_ui_task(
    task_id: int,
    task_text: str,
    on_delete: Callable,
    on_submit: Callable,
    on_change: Callable,
    done: int = 0,
) -> ft.Row:
    task = ft.Row()

    task_field = ft.TextField(value=task_text, expand=True, read_only=True)

    def toggle_edit(event: ft.Event):
        if task_field.read_only:
            task_field.read_only = False
        else:
            task_field.read_only = True

    def submit_action(event: ft.Event):
        text = task_field.value.strip()

        if text:
            on_submit(task_id, text)

    def delete_action(event: ft.Event):
        on_delete(task, task_id)

    toggle_button = ft.IconButton(ft.Icons.EDIT, on_click=toggle_edit)
    submit_button = ft.IconButton(ft.Icons.SAVE, on_click=submit_action)
    delete_button = ft.IconButton(ft.Icons.DELETE, on_click=delete_action)
    checkbox = ft.Checkbox(
        label="Done",
        value=bool(done),
        on_change=lambda x: on_change(checkbox.value, task_id),
    )

    task.controls = [task_field, toggle_button, submit_button, delete_button, checkbox]

    return task
