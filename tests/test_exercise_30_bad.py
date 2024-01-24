# run test on the whole file and find out why does it fail.

import sqlite3
from sqlite3 import Connection

from pytest_tutorial.refactor_exercise.exercise_30_setup_tear_down import add_todo, count_todo


def make_con() -> Connection:
    con = sqlite3.connect(':memory:')
    con.execute("CREATE TABLE todo (task_name TEXT)")
    return con


con = make_con()


def test_add_task():
    add_todo(con, 'task 1')
    assert count_todo(con) == 1

# this test will fail
# def test_add_2_task():
#     add_todo(con, 'task 1')
#     add_todo(con, 'task 2')
#     assert count_todo(con) == 2
