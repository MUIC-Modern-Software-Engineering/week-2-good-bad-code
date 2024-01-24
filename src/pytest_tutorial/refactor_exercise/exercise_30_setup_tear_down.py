from sqlite3 import Connection


# see test in tests/test_exercise_30_setup_tear_down.py

def add_todo(con: Connection, task_name: str) -> None:
    cur = con.cursor()
    cur.execute('INSERT INTO todo (task_name) VALUES (?)', (task_name,))
    con.commit()
    cur.close()


def count_todo(con: Connection) -> int:
    cur = con.cursor()
    cur.execute('SELECT COUNT(*) FROM todo')
    result = cur.fetchone()
    cur.close()
    return result[0]
