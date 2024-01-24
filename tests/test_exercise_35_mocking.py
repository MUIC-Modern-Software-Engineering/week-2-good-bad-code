# cat.ninja will ban us if we make too many requests.
# Let's mock the request to avoid this.
# Not only that but it also returns random fact. We can't test it.
from unittest.mock import MagicMock

import pytest

# read this: https://docs.python.org/3/library/unittest.mock.html
from pytest_tutorial.refactor_exercise.exercise_35_mocking import reverse_cat_fact_api


# IMO: I hate having to mock.
# If you have to mock, you did something wrong.

@pytest.fixture
def mock_cat_fact_api(mocker) -> MagicMock:
    return mocker.patch('requests.get', return_value={'fact': 'cat fact'})


def test_reverse_cat_fact_api(mock_cat_fact_api):
    got = reverse_cat_fact_api()
    assert got == 'tcaf tac'
    mock_cat_fact_api.assert_called_once_with('https://catfact.ninja/fact')
