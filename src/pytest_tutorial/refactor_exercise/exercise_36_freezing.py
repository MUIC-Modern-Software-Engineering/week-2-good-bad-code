import random
from datetime import date, datetime


def random_id() -> str:
    return 'u' + (str(random.randint(0, 9)) * 3)


def my_age() -> int:
    return datetime.now().date().year - 1982
