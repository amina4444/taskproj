import sqlite3
import db.queries as queries
from config import db_path

def init_db(db_path):
    conn = sqlite3.Connection(db_path)

    cursor = conn.cursor()

    cursor.execute(queries.todo_table)

    cursor.close()
    conn.commit()
    conn.close()

def create_task(task: str) -> int:

        conn = sqlite3.Connection(db_path)
 
        cursor = conn.cursor()

        cursor.execute(queries.create_task,(task,))

        id = cursor.lastrowid

        cursor.close()
        conn.commit()
        conn.close()

        return id


def edit_task(id: int, task: str):
    conn = sqlite3.Connection(db_path)

    cursor = conn.cursor()

    cursor.execute(queries.update_task,(task,id))

    cursor.close()
    conn.commit()
    conn.close()

def delete_task(id: int,):
    conn = sqlite3.Connection(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task,(id,))
    cursor.close()
    conn.commit()
    conn.close()


        





   
    