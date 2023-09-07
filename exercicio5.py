#Gerador de Sequência Fibonacci

def gerar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        proximo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo)
    return fibonacci

termos = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))
if termos <= 0:
    print("Por favor, insira um número positivo.")
else:
    resultado = gerar_fibonacci(termos)
    print("Sequência de Fibonacci:", resultado)
