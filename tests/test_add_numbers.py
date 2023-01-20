import unittest

from pytest_tutorial.add_numbers import add_numbers
import pytest


def test_add_numbers():
    got = add_numbers(3, 4)
    assert got == 7


def test_add_numbers_negative():
    got = add_numbers(-1, -2)
    assert got == -3


@pytest.mark.parametrize('a,b,exp', [
    (1, 2, 3),
    (4, 5, 9),
    (0, 0, 0)
])
def test_add_numbers_parametrize(a, b, exp):
    assert add_numbers(a, b) == exp


class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        self.a = 3
        self.b = 2

    def test_basic(self):
        assert add_numbers(1, 2) == 3

    def test_zero_argument(self):
        assert add_numbers(0, 0) == 0

    def test_add_member_field(self):
        print('hello')
        assert add_numbers(self.a, self.b) == 5
