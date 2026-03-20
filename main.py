import flet as ft
import config
from db.main_db import create_task , init_db,edit_task



def main(page: ft.Page):
    main_row = ft.Row()
    tasks_column = ft.Column()

    


    def insert_task(event:ft.Event):
        value = task_text.value

        print(event.control.value)

        def toggle_readonly(_):
            if toggle_readonly:
                task_row.read_only = False
            else:
                task_row.read_only = True

        def submit(_):
            edited_value = task_row.value.strip

            if edited_value:
                edit_task(id,edited_value)
                task_row.read_only=True


        if value.strip():
            id = create_task(value)
            task = ft.Row()
            task_row = ft.TextField(value=value, expand=True,read_only=True)
            task_edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=toggle_readonly)

            sub_edit_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=submit)

            task.controls = [task_row,task_edit_button,sub_edit_button]
            tasks_column.controls.append(task)


    
    task_text = ft.TextField(label="Task", expand=True,on_submit=insert_task)
    enter_button = ft.TextButton(content="Create",icon=ft.Icons.ARROW_FORWARD,on_click=insert_task)

    main_row.controls = [task_text,enter_button]

    page.add(main_row,tasks_column)



if __name__=="__main__":
    init_db(config.db_path)
    ft.run(main, view=ft.AppView.WEB_BROWSER)