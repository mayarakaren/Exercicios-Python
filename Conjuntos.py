#Elementos Únicos: Um conjunto não pode conter elementos duplicados. 
#Se você tentar adicionar o mesmo elemento duas vezes, ele será armazenado apenas uma vez.

conjunto = {1, 2, 3, 3, 4}
print(conjunto)  # Saída: {1, 2, 3, 4}

#Mutabilidade: Os conjuntos são mutáveis, o que significa que você pode adicionar e remover elementos de um conjunto 
#após sua criação.

conjunto = {1, 2, 3}
conjunto.add(4)     # Adiciona o elemento 4 ao conjunto
conjunto.remove(2)  # Remove o elemento 2 do conjunto

#Operações de Conjunto: Python fornece operações de conjuntos, como união, interseção, diferença, e verificação de 
#subconjuntos, que facilitam a manipulação de conjuntos.

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)           # União de conjuntos
intersecao = conjunto1.intersection(conjunto2)  # Interseção de conjuntos

