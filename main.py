import sys

from stats import (
    get_book_text,
    get_chars_frequency,
    get_number_of_words,
    report_char_frequency,
)


def main() -> None:
    book_path: str = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_number_of_words(contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars_frequency = get_chars_frequency(contents)
    print(chars_frequency)
    report_char_frequency(chars_frequency)
    print("============= END ===============")
    return


if __name__ == "__main__":
    main()
