#Calculadora de Média de Notas

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

quantidade_notas = int(input("Quantas notas deseja calcular? "))
notas = []

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)
print(f"A média das notas é: {media}")
