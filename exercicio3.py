#Calculadora Básica

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"Soma: {soma(numero1, numero2)}")
print(f"Subtração: {subtracao(numero1, numero2)}")
print(f"Multiplicação: {multiplicacao(numero1, numero2)}")
print(f"Divisão: {divisao(numero1, numero2)}")
