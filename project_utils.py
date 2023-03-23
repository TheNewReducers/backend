def str_from_file(path) -> str:
    with open(path, 'r') as file:
        text = file.read()

    return text
