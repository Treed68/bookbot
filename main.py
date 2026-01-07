

from stats import get_num_words, get_chars_dict, get_sorted_chars
   
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #chars_dict = get_chars_dict(text)
    chars_sort = get_sorted_chars(text)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at", book_path)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(chars_dict)
    print("--------- Character Count -------")
    for key, value in chars_sort.items():
        print(f"{key}: {value}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()





main()



