import pytest


@pytest.fixture(scope='function')
def magic_list() -> list[int]:
    return [1, 2, 3]
