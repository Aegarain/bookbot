def open_file(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    print(len(open_file(book_path).split()))

main()