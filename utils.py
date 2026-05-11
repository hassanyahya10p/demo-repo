"""Core utility functions."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


def percentage(part, total):
    """Return what percentage `part` is of `total`."""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100


def average(numbers):
    """Return the mean of a list of numbers."""
    if not numbers:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)
