def sort_dictionary(counts):
    result = []
    for letter, count in counts.items():
        if letter.isalpha():
            result.append({"letter": letter, "count": count})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(items):
    return items["count"]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_chars(book_text):
    chars = {}
    for ch in book_text.lower():
        chars[ch] = chars.get(ch, 0) + 1
    return chars