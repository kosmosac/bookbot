import sys
from stats import get_file_contents, get_num_words, get_num_letters, sort_num_letters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #path_to_file = "books/frankenstein.txt"
    path_to_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    file_contents = get_file_contents(path_to_file)
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    # print(f"{num_words} words found in the document")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_num_letters = sort_num_letters(get_num_letters(file_contents))
    # print(sort_num_letters(get_num_letters(file_contents)))
    for letter in list_num_letters:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    
main()
