import re

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def is_email(text):
    if re.fullmatch(regex, text):
        print("Valid email")
    else:
        print("Invalid email")
