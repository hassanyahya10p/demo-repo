"""String / text manipulation utilities."""


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length, appending suffix if cut."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def count_words(text: str) -> int:
    return len(text.split())


def title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())
