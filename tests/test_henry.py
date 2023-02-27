import pytest

from chinaski.henry import path_leaf


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
