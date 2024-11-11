lista = [10,10,4,6,7,8,9,9,11,1,6,5,3]

def remove_repetidos(lista):
    lista1 = []
    for elemento in lista:
        if (elemento not in lista1):
            lista1.append(elemento)
    lista1.sort()
    return lista1

lista = remove_repetidos(lista)
print(lista)

