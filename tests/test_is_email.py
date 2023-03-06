import pytest

from chinaski.is_email import Result, is_email


def test_result_as_str():
    res = Result(is_email=True, email="test@test.com", line_number=1, file_name="test.txt")
    assert "1 - test@test.com - test.txt" == str(res)


@pytest.mark.parametrize(
    "line, expected",
    [
        (
            "test@test.com",
            Result(is_email=True, email="test@test.com", line_number=1, file_name="test.txt"),
        ),
        ("test@test", None),
        ("@test", None),
        ("bad@test.s", None),
        ("bad@test.ss", Result(is_email=True, email="bad@test.ss", line_number=1, file_name="test.txt")),
        ("bad@test.sss", Result(is_email=True, email="bad@test.sss", line_number=1, file_name="test.txt")),
        (
            "secure.secure00000@test.ss",
            Result(is_email=True, email="secure.secure00000@test.ss", line_number=1, file_name="test.txt"),
        ),
        (
            "test@test.es",
            Result(is_email=True, email="test@test.es", line_number=1, file_name="test.txt"),
        ),
        (
            "test@test.fr",
            Result(is_email=True, email="test@test.fr", line_number=1, file_name="test.txt"),
        ),
        (
            "test@test.gov.uk",
            Result(is_email=True, email="test@test.gov.uk", line_number=1, file_name="test.txt"),
        ),
        (
            "test@test.gov.co.uk",
            Result(is_email=True, email="test@test.gov.co.uk", line_number=1, file_name="test.txt"),
        ),
        (
            "test@anything.something.test",
            Result(is_email=True, email="test@anything.something.test", line_number=1, file_name="test.txt"),
        ),
    ],
)
def test_is_email(line, expected):
    assert is_email(line, 1, "test.txt") == expected
