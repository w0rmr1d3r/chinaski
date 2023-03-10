from pathlib import Path
from unittest.mock import patch

import pytest

from chinaski.read_lines import read_lines_from_file

TEST_FILES = Path(__file__).parent / "test_files"


@pytest.mark.parametrize(
    "file, expected",
    [
        (
            f"{TEST_FILES}/one_line_file.txt",
            ["this is a line in a file\n"],
        ),
        (
            f"{TEST_FILES}/several_lines_file.txt",
            [
                "this file has several line\n",
                "\n",
                "in it\n",
                "\n",
                "and can contain an email\n",
                "\n",
                "such as: test@test.com\n",
            ],
        ),
    ],
)
def test_read_lines(file, expected):
    assert read_lines_from_file(filename=file) == expected


def test_read_lines_returns_empty_list_when_file_does_not_exist():
    assert read_lines_from_file(filename="file does not exist") == []


def test_read_lines_returns_empty_list_when_raising_unicode_error():
    with patch("builtins.open") as mock_file:
        mock_file.side_effect = UnicodeDecodeError("funnycodec", b"\x00\x00", 1, 2, "This is just a fake reason!")
        assert read_lines_from_file(filename="unicode_file") == []
    mock_file.assert_called_with("unicode_file", "r")
