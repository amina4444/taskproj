import flet as ft

def create_ui_task(
    task_id: int, task_text:str, on_delete:callable,on_submit:callable
) -> ft.Row:
    task = ft.Row()

    task_field = ft.TextField(value=task_text,expand=True,read_only=True)


   
