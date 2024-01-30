def open_file(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    dict = {'a': 0, 
            'b': 0, 
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0}
    for c in text:
        normalized = c.lower()
        if normalized in dict:
            dict[normalized] +=1
        else:
            dict[normalized] = 1
    return dict


def main():
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    print("Word count:", len(text.split()))
    print(count_letters(text))

main()