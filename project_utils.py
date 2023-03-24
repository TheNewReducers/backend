def str_from_file(path) -> str:
    with open(path, 'r') as file:
        text = file.read()
    return text


def percent_rounded(num_a, num_b) -> int:
    return round((num_a / num_b) * 100)
