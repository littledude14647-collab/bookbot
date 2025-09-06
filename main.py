#takes a text file and turns it into one long string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
#takes a string and counts how many words are in it
def word_count(book_text):
    num_words = 0
    text_list = book_text.split()
    for word in text_list:
        num_words += 1
    return num_words

def main():
    text = get_book_text("books/frankenstein.txt")
    number_words = word_count(text)
    print(f"{number_words} words found in the document")

main()
