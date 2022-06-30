n1 = 0
n2 = 1
lista = []

for x in range(10):
    n3 = n1+n2
    lista.append(n1)
    n1 = n2
    n2 = n3
    
print(lista)
