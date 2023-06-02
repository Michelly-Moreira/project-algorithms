def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    each_letter = [*word]

    if each_letter[low_index] == each_letter[high_index] and high_index != 0:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    elif each_letter[low_index] == each_letter[high_index] and high_index == 0:
        return True
    else:
        return False
    # raise NotImplementedError
