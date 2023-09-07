#Simulação de Jogo de Adivinhação

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
