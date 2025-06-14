import sys
from stats import get_books_text, character_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_books_text(sys.argv[1])
    print("--------- Character Count -------")
    character_count(sys.argv[1])

main()