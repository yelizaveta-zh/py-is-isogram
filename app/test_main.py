from app.main import is_isogram
import pytest


def test_empty_string_is_isogram() -> None:
    assert is_isogram('') is True


def test_isogram_with_unique_letters() -> None:
    assert is_isogram('playgrounds') is True


def test_isogram_with_repeated_letters() -> None:
    assert is_isogram('look') is False


def test_isogram_with_case_insensitivity() -> None:
    assert is_isogram('Adam') is False
