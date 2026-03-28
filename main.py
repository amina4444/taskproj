import flet as ft

import config
from db.main_db import (
    create_task,
    delete_task,
    edit_done,
    edit_task,
    get_tasks,
    init_db,
    delete_done
)
from ui import create_ui_task


def main(page: ft.Page):
    main_row = ft.Row()
    tasks_column = ft.Column()

    def get_tasks_from_db():
        data = get_tasks()

        for task_id, task_text, task_done in data:
            tasks_column.controls.append(
                create_ui_task(
                    task_id,
                    task_text,
                    delete_task_from_ui,
                    edit_task,
                    edit_done,
                    task_done,
                )
            )

    def delete_task_from_ui(task, task_id):
        delete_task(task_id)
        tasks_column.controls.remove(task)

    def insert_task(event: ft.Event):
        value = task_text.value.strip()

        if value:
            task_id = create_task(value)
            task_row = create_ui_task(
                task_id, value, delete_task_from_ui, edit_task, edit_done
            )
            tasks_column.controls.append(task_row)

    
    def del_done(_): 
        delete_done()
        tasks_done = []
        for task in tasks_column.controls:
           if task.controls[-1].value:
            tasks_done.append(task)
        for task in tasks_done:
            tasks_column.controls.remove(task)


    task_text = ft.TextField(label="Задача:", expand=True, on_submit=insert_task)
    enter_button = ft.TextButton(
        content="Создать", icon=ft.Icons.ARROW_FORWARD, on_click=insert_task
    )
    del_done_task = ft.TextButton(content="Очистить выполненные", icon=ft.Icons.DELETE_FOREVER,on_click=del_done)

    get_tasks_from_db()

    main_row.controls = [task_text, enter_button,del_done_task]

    page.add(main_row, tasks_column)


if __name__ == "__main__":
    init_db(config.db_path)
    ft.run(main, view=ft.AppView.WEB_BROWSER)

      