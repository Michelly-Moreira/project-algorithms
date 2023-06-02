def insertion_sort(list_word):
    size_string = len(list_word)
    for letter in range(1, size_string):
        key = list_word[letter]
        new_position = letter - 1
        # enquanto a chave for menor remaneja a letra pra frente
        while new_position >= 0 and list_word[new_position] > key:
            # remaneja a letra
            list_word[new_position + 1] = list_word[new_position]
            new_position -= 1
            # insere a chave na posição correta:
            list_word[new_position + 1] = key


def is_anagram(first_string, second_string):
    result_false = (first_string, second_string, False)
    # se a primeira ou a segunda string não existir:
    if not first_string or not second_string:
        return result_false
    # tornando todas as letras da primeira string em minúsculas
    first_word = first_string.lower()
    # print(first_word)
    # tornando todas as letras da segunda string em minúsculas
    second_word = second_string.lower()
    # print(second_word)

    insertion_sort(first_word)
    insertion_sort(second_word)
    result_true = (first_word, second_word, True)
    result_false = (first_word, second_word, False)
    if first_word == second_word:
        return result_true
    else:
        return result_false

    #  raise NotImplementedError
# print(is_anagram('Perda', 'Pedra'))
