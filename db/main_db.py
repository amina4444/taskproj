import sqlite3

import db.queries as queries
from config import db_path


class SQLiteConnection:
    def __enter__(self):
        self.connection = sqlite3.connect(db_path)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


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

    cursor.execute(queries.create_task, (task,))

    id = cursor.lastrowid

    cursor.close()
    conn.commit()
    conn.close()

    return id


def edit_task(id: int, task: str):
    conn = sqlite3.Connection(db_path)

    cursor = conn.cursor()

    cursor.execute(queries.update_task, (task, id))

    cursor.close()
    conn.commit()
    conn.close()


def delete_task(id: int):
    conn = sqlite3.Connection(db_path)

    cursor = conn.cursor()

    cursor.execute(queries.delete_task, (id,))

    cursor.close()
    conn.commit()
    conn.close()


def get_tasks():
    with SQLiteConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(queries.get_tasks)

        data = cursor.fetchall()
        cursor.close()

    return data


def edit_done(value, id):
    with SQLiteConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(queries.change_done, (value, id))
        conn.commit()
 
def delete_done():
    with SQLiteConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(queries.delete_done )
        conn.commit()




        





   
    