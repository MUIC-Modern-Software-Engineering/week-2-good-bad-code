# see also setup teardown in pytest doc you can do a class based one too.
import sqlite3
from sqlite3 import Connection
from typing import Generator

import pytest

from pytest_tutorial.refactor_exercise.exercise_30_setup_tear_down import add_todo, count_todo


@pytest.fixture(scope='function')
def con() -> Generator[Connection, None, None]:
    con = sqlite3.connect(':memory:')
    con.execute("CREATE TABLE todo (task_name TEXT)")
    yield con
    con.close()


def test_add_task(con: Connection):
    add_todo(con, 'task 1')
    assert count_todo(con) == 1


def test_add_2_task(con: Connection):
    add_todo(con, 'task 1')
    add_todo(con, 'task 2')
    assert count_todo(con) == 2


# this get magic list from conftest.py (see pytest doc)
def test_add_stuff_to_magic_list(magic_list: list[int]):
    magic_list.append(4)
    assert magic_list == [1, 2, 3, 4]


def test_remove_stuff_to_magic_list(magic_list: list[int]):
    magic_list.append(4)
    assert magic_list == [1, 2, 3, 4]
