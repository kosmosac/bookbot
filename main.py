from stats import get_file_contents, get_num_words, get_num_letters

def main():
    file_contents = get_file_contents("books/frankenstein.txt")
    num_words = get_num_words(file_contents)
    print(f"{num_words} words found in the document")
    print(get_num_letters(file_contents))
    
main()
