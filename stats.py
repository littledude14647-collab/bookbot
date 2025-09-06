#takes a string and counts how many words are in it
def word_count(book_text):
    num_words = 0
    text_list = book_text.split()
    for word in text_list:
        num_words += 1
    return num_words