"""Input validation helpers."""
import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    """Accepts E.164 format: +<country><number>, 7–15 digits."""
    pattern = r"^\+[1-9]\d{6,14}$"
    return bool(re.match(pattern, phone))


def is_non_empty_string(value) -> bool:
    return isinstance(value, str) and len(value.strip()) > 0


def is_positive_integer(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0
