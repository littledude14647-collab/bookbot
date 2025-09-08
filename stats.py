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

def sort_on(items):
    return items["num"]

def dictionary_sorter(dictionary):
    sorted_list = []
    for char in dictionary:
        temp_dict = {}
        temp_dict = {
            "char": char, "num": dictionary[char]
        }
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


