from chinaski.is_email import is_email
from chinaski.read_lines import read_lines_from_file


def chinaski(file: str):
    print("hello world")
    print(file)
    lines = read_lines_from_file(filename=file)
    for line in lines:
        is_email(line)
    print("bye world")
