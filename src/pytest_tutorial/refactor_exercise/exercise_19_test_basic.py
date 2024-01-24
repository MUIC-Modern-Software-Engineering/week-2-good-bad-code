from typing import TypeVar

T = TypeVar('T')


def add_number(a: int, b: int) -> int:
    return a + b


def reverse_list(lst: list[T]) -> list[T]:
    return lst[::-1]


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
