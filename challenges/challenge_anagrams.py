def insertion_sort(list_word):
    size_string = len(list_word)
    list_word = [*list_word]
    for letter in range(1, size_string):
        key = list_word[letter]
        # print('letra que o for trouxe como chave:', key)
        new_position = letter - 1
        # print('posição anterior pra iniciar a comparação:', new_position)
        # enquanto a chave for menor remaneja a letra pra frente
        while new_position >= 0 and key < list_word[new_position]:
            # remaneja a letra
            # print('letra a ser remanejada:', list_word[new_position + 1])
            # print('compara com:', list_word[new_position])
            list_word[new_position + 1] = list_word[new_position]
            # r = u
            # print(list_word)
            new_position -= 1

            # insere a chave na posição correta:
        list_word[new_position + 1] = key
        # print('depois de inserir na posição correta',list_word)
        # unindo as strings ordenadas formando a palavra
    return ''.join(list_word)

def is_anagram(first_string, second_string):
    # tornando todas as letras da primeira string em minúsculas
    first_word = first_string.lower()
    # print(first_word)
    # tornando todas as letras da segunda string em minúsculas
    second_word = second_string.lower()
    # print(second_word)
    first_word = insertion_sort(first_word)
    second_word = insertion_sort(second_word)
    result_true = (first_word, second_word, True)
    result_false = (first_word, second_word, False)
     # se a primeira ou a segunda string não existir:
    if not first_string or not second_string:
        return result_false
    elif len(first_word) != len(second_word):
        return result_false
    elif first_word == second_word:
        return result_true
    else:
        return result_false

    #  raise NotImplementedError

# print(is_anagram('muro', 'rumo'))
# print(insertion_sort('muro'))
