# C-R-U-D

todo_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task STRING NOT NULL,
    done INTEGER DEFAULT 0
    );
"""

# C - создание

create_task = """
    INSERT INTO tasks (task) VALUES (?);
"""

# R - чтение
get_tasks = """
    SELECT id, task, done FROM tasks;
"""

# U - обновление
update_task = """
    UPDATE tasks SET task = ? WHERE id = ?;
"""

# D - удаление
delete_task = """
    DELETE FROM tasks WHERE id = ?;
"""

change_done = """
    UPDATE tasks SET done = ? WHERE id = ?
"""

delete_done = """
    DELETE FROM tasks WHERE done = 1
"""