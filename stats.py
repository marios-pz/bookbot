def get_book_text(input_file_path: str):
    with open(input_file_path) as f:
        file_contents = f.read()
        return file_contents


def get_number_of_words(contents: str):
    num_words = len(contents.split())
    return num_words


def get_chars_frequency(contents: str) -> dict[str | int]:
    chars_frequency = {}

    # initialize NOTE: improve this
    for char in contents:
        char = char.lower()
        chars_frequency[char] = 0

    for char in contents:
        char = char.lower()
        chars_frequency[char] += 1

    return chars_frequency


def report_char_frequency(chars_frequency: dict[str | int]) -> None:

    sorted_chars = sorted(chars_frequency.items())

    for key, value in sorted_chars:
        if key.isalpha():
            print(f"{key}: {value}")
