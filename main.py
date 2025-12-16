from stats import get_letter_count, get_word_count, get_letter_count, sorted_list
import sys


def get_book_text(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        word_count = get_word_count(book_text)
        letter_count = get_letter_count(book_text)
        sorted_letters = sorted_list(letter_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for item in sorted_letters:
            char = item["char"]
            num = item["num"]
            if char.isalpha():
                print(f"{char}: {num}")

        print("============= END ===============")

main()
