# c-r-u-d

todo_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    task STRING NOT NULL

    );

"""

# c - создание

create_task = """
    INSERT INTO tasks (task) VALUES (?);
"""

# r - чтение 

get_tasks = """
   SELECT  id, task FROM tasks;
"""

# u - обновление 

update_task = """
     UPDATE tasks SET task = ?WHERE id = ?;
"""
# d - удаление
delete_task = """
    DELETE FROM tasks WHERE id = ?;
"""