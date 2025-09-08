from stats import word_count
from stats import character_count
from stats import dictionary_sorter
#takes a text file and turns it into one long string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    number_words = word_count(text)
    number_chars = character_count(text)
    sorted_list = dictionary_sorter(number_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    
main()
