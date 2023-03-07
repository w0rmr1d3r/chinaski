from pathlib import Path, PosixPath
from unittest import TestCase
from unittest.mock import patch

import pytest
from _pytest.python_api import raises

from chinaski.henry import (
    PathToFileOrDirIsNotValidException,
    assert_given_path_is_valid,
    core,
    obtain_list_of_files,
    path_leaf,
)
from chinaski.is_email import Result

TEST_FILES = Path(__file__).parent / "test_files"


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


def test_core_directory():
    result = core(str(TEST_FILES))

    # asserting this way to pass the test, since sorting isn't available for Result
    assert len(result) == 3
    assert Result(is_email=True, email="test@test.com", line_number=7, file_name="several_lines_file_two.txt") in result
    assert (
        Result(is_email=True, email="super@email.net", line_number=9, file_name="several_lines_file_two.txt") in result
    )
    assert Result(is_email=True, email="test@test.com", line_number=7, file_name="several_lines_file.txt") in result


@pytest.mark.parametrize(
    "invalid_file_path",
    [
        "",
        None,
    ],
)
def test_core_raises_exception_if_file_path_is_not_valid(invalid_file_path):
    with raises(PathToFileOrDirIsNotValidException):
        _ = core(invalid_file_path)


@pytest.mark.parametrize(
    "invalid_file_path",
    [
        "",
        None,
    ],
)
def test_assert_given_path_is_valid_raises_exception_if_file_path_is_not_valid(invalid_file_path):
    with raises(PathToFileOrDirIsNotValidException):
        assert_given_path_is_valid(invalid_file_path)


def test_obtain_list_of_files_single_file():
    result = obtain_list_of_files(TEST_FILES / "one_line_file.txt")

    expected = [TEST_FILES / "one_line_file.txt"]

    assert result == expected


def test_obtain_list_of_files_directory():
    result = obtain_list_of_files(TEST_FILES)

    expected = [
        PosixPath(TEST_FILES / "several_lines_file_two.txt"),
        PosixPath(TEST_FILES / "several_lines_file.txt"),
        PosixPath(TEST_FILES / "one_line_file.txt"),
    ]

    # sorted to pass the test, but order is not important
    TestCase().assertListEqual(sorted(result), sorted(expected))


@pytest.mark.parametrize(
    "path_to_ignore",
    [
        ".git",
        ".git/",
        "/.git/test",
        "/.idea/test",
        "/.pytest_cache/test",
        "/__pycache__/test",
    ],
)
def test_obtain_list_of_files_ignores_path(path_to_ignore):
    assert obtain_list_of_files(path_to_ignore) == []
