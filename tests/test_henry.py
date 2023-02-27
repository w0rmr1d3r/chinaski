from unittest.mock import patch

import pytest
from _pytest.python_api import raises

from chinaski.henry import FilePathIsNotValidException, core, path_leaf
from chinaski.is_email import Result


@pytest.mark.parametrize(
    "line_input, expected",
    [
        ("a/b/c/", "c"),
        ("a/b/c", "c"),
        ("\\a\\b\\c", "c"),
        ("\\a\\b\\c\\", "c"),
        ("a\\b\\c", "c"),
        ("a/b/../../a/b/c/", "c"),
        ("a/b/../../a/b/c", "c"),
    ],
)
def test_path_leaf(line_input, expected):
    result = path_leaf(line_input)
    assert result == expected


@patch("chinaski.read_lines.read_lines_from_file")
def test_core(mock_read_lines_from_file):
    mock_read_lines_from_file.return_value = [
        "line of first file test@test.com",
        "line without an email",
        "var email = test2@test.com;",
    ]

    result = core("file.txt")

    expected = [
        Result(is_email=True, email="test@test.com", line_number=1, file_name="file.txt"),
        Result(is_email=True, email="test2@test.com", line_number=3, file_name="file.txt"),
    ]

    assert result == expected


@pytest.mark.parametrize(
    "invalid_file_path",
    [
        "",
        None,
    ],
)
def test_core_raises_exception_if_file_path_is_not_valid(invalid_file_path):
    with raises(FilePathIsNotValidException):
        _ = core(invalid_file_path)
