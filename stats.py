def get_num_words():
    with open ("./books/frankenstein.txt") as f:    # do something with f (the file) here
        file_contents = f.read()      # f is a file object
        words = file_contents.split()
    count = 0
    for word in words:
        count += 1
   
    print (f"Found {count} total words")
    #return count


def count_characters():
    characters_dict = {}   #create characters dictionary
    with open ("./books/frankenstein.txt") as f:    # do something with f (the file) here
        file_contents = f.read()      # f is a file object
        low_character = file_contents.lower() #return lower case of text
        for character in low_character:
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] =1    
        print (characters_dict)
        return characters_dict





    



get_num_words()
count_characters()

