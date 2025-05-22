from stats import get_words_count, get_characters_count, sort_characters, print_characters
import sys

def get_book_text(book_path):
    # open a file using path to file string, place the file in f
    with open(book_path) as f:
        # read f contents using read() and store it in book_contents variable to use later
        book_contents = f.read()
        return book_contents

def main():
    args = sys.argv
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = get_book_text(args[1])
    num_words = get_words_count(book_contents)
    print(f"Found {num_words} total words")
    characters_count = get_characters_count(book_contents)
    sorted_characters= sort_characters(characters_count)
    print_characters(sorted_characters)

main()