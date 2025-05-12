def get_word_count(string):
    words = string.split()
    num_words = len(words)
    return num_words

def get_character_count(string):
    chars = {}
    lowered_str = string.lower()
    for letter in lowered_str:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    
    result = []
    for char, count in chars.items():
        result.append({"char": char, "num": count})

    return sort_dict(result)

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict