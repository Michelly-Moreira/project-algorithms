def insertion_sort(list_word):
    size_string = len(list_word)
    for letter in range(1, size_string):
        key = list_word[letter]
        new_position = letter -1
        while new_position >= 0 and list_word[new_position] > key:# enquanto a chave for menor remaneja a letra pra frente
            list_word[new_position + 1] = list_word[new_position]# remaneja a letra
            new_position -= 1
            list_word[new_position + 1] = key# insere a chave na posição correta


def is_anagram(first_string, second_string):
    if not first_string or not second_string:# se a primeira ou a segunda string não existir
        return (first_string, second_string, False)
    
    first_word = first_string.lower()# tornando todas as letras da primeira string em minúsculas
    # print(first_word)
    second_word = second_string.lower()# tornando todas as letras da segunda string em minúsculas
    # print(second_word)

    insertion_sort(first_word)
    insertion_sort(second_word)

    if first_word == second_word:
        return (first_word, second_word, True)
    else:
        return (first_word, second_word, False)

    #raise NotImplementedError

# print(is_anagram('Perda', 'Pedra'))