def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_chars(text):
    chars_sort = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars_sort:
            chars_sort[lowered] += 1
        else:
            chars_sort[lowered] = 1
    
    dict_sort ={key: value for key,
                value in sorted(chars_sort.items(), 
                                reverse=True,
                                key=lambda item: item[1])
                                if key.isalpha()}
    
        
    
    return dict_sort
    

    



    

