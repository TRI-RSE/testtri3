import pytest

from testtri3 import count_words, remove_whitespace, reverse_string, to_title_case


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    assert reverse_string("Hello World") == "dlroW olleH"


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("python programming") == "Python Programming"


def test_to_title_case_already_title():
    assert to_title_case("Already Title") == "Already Title"


def test_remove_whitespace():
    assert remove_whitespace("Hello World") == "HelloWorld"
    assert remove_whitespace("  spaces  everywhere  ") == "spaceseverywhere"


def test_remove_whitespace_no_spaces():
    assert remove_whitespace("NoSpaces") == "NoSpaces"


def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("The quick brown fox") == 4


def test_count_words_single_word():
    assert count_words("Hello") == 1


def test_count_words_empty_string():
    assert count_words("") == 0


def test_count_words_multiple_spaces():
    assert count_words("Hello   World   Test") == 3
