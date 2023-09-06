7 != 3 and 2 > 3

#Tabela verdade do AND

True and True
True and False
False and True
False and False

#Tabela verdade do OU

True or True
True or False
False or True
False or False

#Tabela verdade do XOR (ou exclusivo)

True != True
True != False
False != True
False != False

#Operador de negação

not True
not False

not 0
not 1
not not -1
not not True

#Operadores para tomar cuidado
#bit a bit - não utlizar

True & False
False | True
True ^ False

#Exemplo

saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)
