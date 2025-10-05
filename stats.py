import sys

def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    counter = {}
    for letter in book:
        letter = letter.lower()
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

# python
def sort_on(item):
    return item["num"]

def most_common(counter):
    items = []
    for char, num in counter.items():
        items.append({"char": char, "num": num})
    items.sort(reverse=True, key=sort_on)
    return items

print(sys.argv)