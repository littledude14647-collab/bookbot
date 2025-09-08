from stats import word_count
from stats import character_count
from stats import dictionary_sorter
import sys
#takes a text file and turns it into one long string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        input = sys.argv[1]
        
    text = get_book_text(f"{input}")
    number_words = word_count(text)
    number_chars = character_count(text)
    sorted_list = dictionary_sorter(number_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input}...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    
main()
