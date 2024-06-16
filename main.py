def main():
    book_path = 'books/frankenstein.txt'
    print(f'--- Begin report of {book_path} ---')

    book_contents = get_book_contents(book_path)

    book_word_count = get_word_count(book_contents)
    print(f"{book_word_count} words found in the document\n")

    book_unique_letters = get_unique_letters(book_contents)
    print(f"unique letter count: {book_unique_letters}")

    print('--- End report ---')


def get_book_contents(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)


def get_unique_letters(file_contents):
    counts = {}
    for i in file_contents.lower():
        counts[i] = counts.get(i, 0) + 1
    return counts


main()
