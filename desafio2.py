#Uma pessoa tem dois trabalhos para realizar, um na terça e um na quarta, se dois trabalhos derem certo a pessoa vai no shopping comprar uma televisão de 50 polegadas, e se apenas um der certo irá comprar uma televisão de 32 polegadas

"""
Confirmando os 2: Tv 50' + Sorvete
Confirmando apenas 1: Tv 32' + Sorvete
Nenhum confirmado: Fica em casa
"""

trabalho_terca = input("O trabalho de Terça foi concluído? (True ou False):")
trabalho_quinta = input("E o trabalho de quinta? (True ou False):")

if trabalho_terca == "True" and trabalho_quinta == "True":
    print("Televisão de 50 polegadas + Sorvete")
elif trabalho_terca == "True" and trabalho_quinta == "False":
    print("Televisão de 32 polegadas + Sorvete")
elif trabalho_terca == "False" and trabalho_quinta == "True":
    print("Televisão de 32 polegadas + Sorvete")
else:
    print("Fique em Casa!")

#---------------------------------------------------------------

#Outra forma apenas com Operadores

terca = False
quinta = False

tv50 = terca and quinta
sorvete = terca or quinta
tv32 = terca != quinta
saude = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saúde={}"
      .format(tv50, tv32, sorvete, saude))