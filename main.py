# python
from stats import word_count, char_count, most_common
import sys



def main():
    if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    counts = char_count(text)
    chars = most_common(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    for item in chars:
        c = item["char"]
        if c.isalpha():
            print(f"{c}: {item['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()