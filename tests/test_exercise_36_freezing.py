import random

from freezegun import freeze_time

from pytest_tutorial.refactor_exercise.exercise_36_freezing import my_age, random_id


@freeze_time('2023-01-22')
def test_my_age():
    got = my_age()
    assert got == 41


def test_random_id():
    random.seed(555)
    got = random_id()
    assert len(got) == 4
    assert got.startswith('u')
    assert got[1:].isdigit()
