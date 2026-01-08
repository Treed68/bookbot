import sys

if len(sys.argv)<2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


from stats import (
    get_num_words, 
    get_chars_dict, 
    get_sorted_chars
)   
    

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sort = get_sorted_chars(text)
    print_report(book_path, num_words, chars_sort)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sort):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in chars_sort.items():
        print(f"{key}: {value}")
    print("============= END ===============")




main()



