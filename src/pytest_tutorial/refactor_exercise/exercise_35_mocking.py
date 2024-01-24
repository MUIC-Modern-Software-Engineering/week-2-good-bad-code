import requests


def reverse_cat_fact_api() -> str:
    response = requests.get("https://catfact.ninja/fact")
    return response["fact"][::-1]


def get_cat_fact() -> str:
    response = requests.get("https://catfact.ninja/fact")
    return response["fact"]


def reverse(s: str) -> str:
    return s[::-1]


def better_reverse_cat_fact_api():
    return reverse(get_cat_fact())
