import pytest

from chinaski.finder import find_emails_in_line


@pytest.mark.parametrize(
    "line_input, expected",
    [
        ("", []),
        ("user@mail.test\n", ["user@mail.test"]),
        ("super shor text with an email user@mail.test", ["user@mail.test"]),
        ("var username = user@mail.test", ["user@mail.test"]),
        ("fake@ss", []),
        ("@source", []),
    ],
)
def test_find_emails_in_line(line_input, expected):
    result = find_emails_in_line(line_input)
    assert result == expected
