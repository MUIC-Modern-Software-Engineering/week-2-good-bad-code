import pytest
from pytest import approx

from pytest_tutorial.refactor_exercise.exercise_19_test_basic import reverse_list, divide


def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]


def test_reverse_list_empty():
    assert reverse_list([]) == []


def test_divide():
    assert divide(4, 2) == 2
    assert divide(4, 3) == approx(1.33, abs=0.01)


def test_divide_by_zero_should_raise_value_error():
    with pytest.raises(ValueError):
        divide(4, 0)
