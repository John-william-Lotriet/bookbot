def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = text_to_num_of_words(text)
    letter_counts = count_letters(text)
    letter_counts_list = list(letter_counts.items())
    letter_counts_list.sort(key=None, reverse=False)

    print(f"Book report for the book {book_path}\n")
    print(f"This book contains {word_count} words\n")

    for letter, count in letter_counts_list:
        print(f"The '{letter}' character was found {count} times")

    print("End report")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def text_to_num_of_words(text):
    return len(text.split())

def count_letters(text):
        text = text.lower()
        letter_counts = {}
        for letter in text:
            if letter.isalpha():
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1
        return letter_counts



main()