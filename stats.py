def get_words_count(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_characters_count(book_contents):
    characters_count = {}
    for char in list(book_contents.lower()):
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
    return characters_count

def sort_on(dict):
    return dict["num"]

def sort_characters(characters_count):
    sorted_characters = []
    for k in characters_count:
        sorted_characters.append({'character':k, 'num': characters_count[k]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
    
def print_characters(sorted_characters):
    for char in sorted_characters:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["num"]}")