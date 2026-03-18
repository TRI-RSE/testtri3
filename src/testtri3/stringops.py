def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def to_title_case(text: str) -> str:
    """Convert text to title case."""
    return text.title()


def remove_whitespace(text: str) -> str:
    """Remove all whitespace from text."""
    return "".join(text.split())


def count_words(text: str) -> int:
    """Count the number of words in text."""
    return len(text.split())
