from stats import count_words, count_letters, sort_letters_dict
import sys

def get_book_text(path):
    res = None
    with open(path, 'r') as f:
        res = f.read()
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for val in sort_letters_dict(count_letters(text)):
        print(f"{val["char"]}: {val["num"]}")
    print("============= END ===============")

main()