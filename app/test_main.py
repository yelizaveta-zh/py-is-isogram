from app.main import is_isogram
import pytest



def test_empty_string_is_isogram() -> None:
    """Test that an empty string is an isogram."""
    assert is_isogram('') is True


def test_isogram_with_unique_letters() -> None:
    """Test that a string with all unique letters is an isogram."""
    assert is_isogram('playgrounds') is True


def test_isogram_with_repeated_letters() -> None:
    """Test that a string with repeated letters is not an isogram."""
    assert is_isogram('look') is False


def test_isogram_with_case_insensitivity() -> None:
    """Test that the function is case-insensitive."""
    assert is_isogram('Adam') is False


def test_isogram_with_mixed_case_unique_letters() -> None:
    """Test that a string with mixed case unique letters is an isogram."""
    assert is_isogram('Python') is True


def test_isogram_with_special_case() -> None:
    """Test edge case with single letter."""
    assert is_isogram('A') is True

