def is_palindrome_recursive(word, low_index, high_index):
    each_letter = [*word]
    low_index += 1
    inverted_letters = each_letter[::-1]

    if not word:
        return False
    elif low_index >= high_index:
        return True
    elif each_letter == inverted_letters:
        return True and is_palindrome_recursive(word, low_index, high_index)
    else:
        return False
    # raise NotImplementedError

print(is_palindrome_recursive('', 0, -1))