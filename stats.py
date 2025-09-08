#takes a string and counts how many words are in it
def word_count(book_text):
    text_list = book_text.split()
    return len(text_list)

def character_count(book_text):
    characters = {}
    for char in book_text:
        lowchar = char.lower()
        try:
            characters[lowchar] += 1
        except KeyError:
            characters[lowchar] = 1
    return characters