#Encontrar Elementos Únicos em uma Lista

def elementos_unicos(lista):
    conjunto_unico = set()
    for elemento in lista:
        if lista.count(elemento) == 1:
            conjunto_unico.add(elemento)
    return list(conjunto_unico)

lista_numeros = [1, 2, 3, 2, 4, 5, 6, 5, 7, 7, 8, 9, 0]
unicos = elementos_unicos(lista_numeros)
print("Elementos únicos na lista:", unicos)
