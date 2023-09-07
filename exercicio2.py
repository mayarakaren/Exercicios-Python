#Contagem de Palavras em uma Frase

frase = input("Digite uma frase: ")
palavras = frase.split() #dividi a frase em palavras
numero_palavras = len(palavras) #conta a quantidade de palavras
print(f"A frase tem {numero_palavras} palavra(s).")
