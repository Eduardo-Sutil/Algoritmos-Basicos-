def bubble_sort(lista):
    for x in range(len(lista)-1):
        ja_sortedo = True

        for z in range(0, len(lista)-1):
            if lista[z] > lista[z+1]:
                lista[z], lista[z+1] = lista[z+1], lista[z]
                ja_sortedo = False

            if ja_sortedo:
                break

    return lista

print(bubble_sort([3, 2, 1]))
