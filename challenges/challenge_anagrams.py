def merge_sort(list_word, start=0, end=None):
    if end is None:
        end = len(list_word)
        # linha 5: se não reduzi o suficiente, continua
    if (end - start) > 1:
        # encontrando o meio:
        mid = (start + end) // 2
        # dividindo as listas:
        merge_sort(list_word, start, mid)
        merge_sort(list_word, mid, end)
        # unindo as listas
        merge(list_word, start, mid, end)


# função auxiliar que realiza a mistura dos dois arrays

def merge(list_word, start, mid, end):
    # indexando a lista da esquerda:
    left = list_word[start:mid]
    # indexando a lista da direita
    right = list_word[mid:end]
    # as duas listas começarão do início
    left_index, right_index = 0, 0
    # percorrer sobre a lista inteira como se fosse uma:
    for general_index in range(start, end):
        # se os elementos da esquerda acabaram,
        # preenche o restante com a lista da direita:
        if left_index >= len(left):
            list_word[general_index] = right[right_index]
            right_index = right_index + 1
            # se os elementos da direita acabaram,
            # preenche o restante com a lista da esquerda:
        elif right_index >= len(right):
            list_word[general_index] = left[left_index]
            left_index = left_index + 1
            # se o elemento do topo da esquerda for menor que o da direita,
            # ele será o escolhido:
        elif left[left_index] < right[right_index]:
            list_word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            # caso o da direita seja menor, ele será o escolhido
            list_word[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    # tornando todas as letras da primeira string em minúsculas
    first_word = first_string.lower()
    # print(first_word)
    # tornando todas as letras da segunda string em minúsculas
    second_word = second_string.lower()
    # print(second_word)
    list_word = [*first_word]
    merge_sort(list_word, 0, len(list_word))
    first_word = ''.join(list_word)
    list_word = [*second_word]
    merge_sort(list_word, 0, len(list_word))
    second_word = ''.join(list_word)
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
# print(merge('muro'))
