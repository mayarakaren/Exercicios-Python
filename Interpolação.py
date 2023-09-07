#Formatação de Strings (Python 3.6+):
#Com a introdução das "f-strings" (format strings) no Python 3.6, a interpolação de strings ficou mais simples e legível. 
#Você pode incorporar expressões Python diretamente em strings prefixadas com f ou F. As variáveis e expressões entre chaves {} são avaliadas e inseridas na string.

nome = "Alice"
idade = 30
mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos."
print(mensagem)
# Saída: "Olá, meu nome é Alice e tenho 30 anos."

#Método str.format() (Python 2.7+ e 3.x):
#Antes das f-strings, o método str.format() era comumente usado para interpolação de strings. 
#Você pode criar uma string com espaços reservados {} e, em seguida, usar o método .format() para preencher os espaços reservados com valores.

nome = "Alice"
idade = 30
mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome, idade)
print(mensagem)
# Saída: "Olá, meu nome é Alice e tenho 30 anos."

#Operador % (Python 2.x):
#Em versões mais antigas do Python (2.x), o operador % era usado para interpolação de strings. Ele funciona de maneira semelhante ao método str.format().

nome = "Alice"
idade = 30
mensagem = "Olá, meu nome é %s e tenho %d anos." % (nome, idade)
print(mensagem)
# Saída: "Olá, meu nome é Alice e tenho 30 anos."







