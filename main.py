from stats import word_count
#takes a text file and turns it into one long string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    number_words = word_count(text)
    print(f"{number_words} words found in the document")

main()
