def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def sort_on(items):
    return items["num"]

def sorted_list(letter_count):
    letter_count_list = []
    for letter, count in letter_count.items():
        letter_count_list.append({"char": letter, "num": count})
    letter_count_list.sort(reverse=True, key=sort_on)
    return letter_count_list


def get_letter_count(book_text):
    letter_count = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count
