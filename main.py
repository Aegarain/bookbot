def open_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {}
    for c in text:
        normalized = c.lower()
        if normalized in dict:
            dict[normalized] +=1
        else:
            dict[normalized] = 1
    return dict

def sortkey(n):
    return n[1]


def sort_char_count(char_count):
    sorted_list = []
    for x in char_count:
        sorted_list.append((x,char_count[x]))
    sorted_list.sort(reverse = True, key = sortkey)
    return(sorted_list)

def report(book_path):
    text = open_file(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_char_count(char_count)
    rep = f"{word_count} words found in the document\n\n"
    for x in sorted_char_count:
        if not x[0].isalpha():
            continue
        rep += f"The '{x[0]}' character was found {x[1]} times\n"
    return rep

def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    print(report(book_path))
    print("--- End report ---")

main()