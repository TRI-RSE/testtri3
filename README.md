# testtri3

A simple Python library for string utilities.

## Installation

```bash
pip install testtri3
```

Or install locally in development mode:

```bash
pip install -e .
```

## Usage

```python
from testtri3 import reverse_string, to_title_case, remove_whitespace, count_words

# Reverse a string
reversed_text = reverse_string("Hello, world!")
print(reversed_text)  # !dlrow ,olleH

# Convert to title case
title = to_title_case("hello world from python")
print(title)  # Hello World From Python

# Remove all whitespace
cleaned = remove_whitespace("Hello   World  ")
print(cleaned)  # HelloWorld

# Count words
word_count = count_words("The quick brown fox")
print(word_count)  # 4
```

## API

| Function | Description |
|---|---|
| `reverse_string(text)` | Reverse a string |
| `to_title_case(text)` | Convert text to title case |
| `remove_whitespace(text)` | Remove all whitespace from text |
| `count_words(text)` | Count the number of words in text |

## Running Tests

```bash
pip install pytest
pytest tests/
```
