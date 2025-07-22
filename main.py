import sys

sys.argv

if len(sys.argv) >1:
    book_path = ''.join(sys.argv[1:])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_num_words, get_chars_dict, sort_char_counts


def main():
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_char_counts(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
