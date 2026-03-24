import flet as ft
import config
from db.main_db import create_task , init_db,edit_task,delete_task



def main(page: ft.Page):
    main_row = ft.Row()
    tasks_column = ft.Column()

    def insert_task(event: ft.Event):
        value = task_text.value.strip()

        if value:
            task_id = create_task(value)

            task_row = ft.TextField(value=value, expand=True, read_only=True)

            def toggle_readonly(_):
                if task_row.read_only:
                    task_row.read_only = False
                else:
                    task_row.read_only = True

            def submit(_):
                edited_value = task_row.value.strip()
                if edited_value:
                    edit_task(task_id, edited_value)
                    task_row.read_only = True
                   

            def delete(_):
                delete_task(task_id)
                tasks_column.controls.clear()
            

            toggle_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=toggle_readonly)
            submit_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=submit)
            delete_button = ft.IconButton(icon=ft.Icons.DELETE,icon_color=ft.Colors.RED_900, on_click=delete)

            task = ft.Row([task_row,toggle_button,submit_button,delete_button ])

            tasks_column.controls.append(task)
            task_text.value = ""
            

    task_text = ft.TextField(label="Task", expand=True, on_submit=insert_task)
    enter_button = ft.TextButton("Create", icon=ft.Icons.ARROW_FORWARD, on_click=insert_task)

    main_row.controls = [task_text, enter_button]

    page.add(main_row, tasks_column)
   




if __name__=="__main__":
    init_db(config.db_path)
    ft.run(main, view=ft.AppView.WEB_BROWSER)