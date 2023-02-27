import pytest

from chinaski.is_email import Result, is_email


def test_result_as_str():
    res = Result(is_email=True, email="test@test.com", line_number=1, file_name="test.txt")
    assert "1 - test@test.com - test.txt" == str(res)


@pytest.mark.parametrize(
    "line, line_number, file_name, expected",
    [
        (
            "test@test.com",
            1,
            "test.txt",
            Result(is_email=True, email="test@test.com", line_number=1, file_name="test.txt"),
        ),
        ("test@test", 1, "test.txt", None),
        ("@test", 1, "test.txt", None),
        ("bad@test.s", 1, "test.txt", None),
    ],
)
def test_is_email(line, line_number, file_name, expected):
    assert is_email(line, line_number, file_name) == expected
