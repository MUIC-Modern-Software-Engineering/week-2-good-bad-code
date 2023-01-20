from dataclasses import dataclass


@dataclass
class User:
    name: str


def validate_user(user: User, throw_if_error: bool) -> bool:
    """Validate User.

    Args:
        user (User):

    Returns:
        True if user is valid. False otherwise.
    """
    ...
