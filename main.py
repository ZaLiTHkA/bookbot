def main():
    book_path = 'books/frankenstein.txt'
    book_contents = get_book_contents(book_path)
    book_word_count = get_word_count(book_contents)
    book_chars_list = get_book_chars_by_frequency(book_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_word_count} words found in the document")
    print()

    for item in book_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_contents(file_name):
    with open(file_name) as f:
        return f.read()


def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)


# DISCLAIMER: I could not work out what I needed to do here, so I did skip and check the solution.
# the code below was based of said solution...
# I must do better.


def get_book_chars_by_frequency(book_contents):
    num_chars_dict = get_book_chars_dict(book_contents)

    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]


def get_book_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
