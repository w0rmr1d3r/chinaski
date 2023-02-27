def read_lines_from_file(filename) -> list:
    with open(filename, "r") as file:
        return file.readlines()
