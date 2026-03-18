from importlib.metadata import PackageNotFoundError, version

from .stringops import count_words, remove_whitespace, reverse_string, to_title_case

__all__ = ["reverse_string", "to_title_case", "remove_whitespace", "count_words"]

try:
    __version__ = version("testtri3")
except PackageNotFoundError:
    __version__ = "unknown"
