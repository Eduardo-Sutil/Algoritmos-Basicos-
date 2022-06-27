def selection_sort(lista):
    for j in range(len(lista)-1):
        min_index = j
        for x in range(j, len(lista)):
            if lista[x] < lista[min_index]:
                min_index = x

            if lista[j] > lista[min_index]:
                lista[j], lista[min_index] = lista[min_index], lista[j]

    return lista

print(selection_sort([3,2,1,5,7,8,9]))







