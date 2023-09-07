# Conversor de Moedas

taxas_de_cambio = {
    "USD": 1.0,     # Dólar Americano (taxa base)
    "EUR": 0.85,    # Euro
    "JPY": 110.0,   # Iene Japonês
    "GBP": 0.73,    # Libra Esterlina
}

def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem in taxas_de_cambio and moeda_destino in taxas_de_cambio:
        taxa_origem = taxas_de_cambio[moeda_origem]
        taxa_destino = taxas_de_cambio[moeda_destino]
        valor_convertido = valor * (taxa_destino / taxa_origem)
        return valor_convertido
    else:
        return None

moeda_origem = input("Digite a moeda de origem: ")
moeda_destino = input("Digite a moeda de destino: ")
valor = float(input("Digite o valor a ser convertido: "))

resultado = converter_moeda(valor, moeda_origem, moeda_destino)
if resultado is not None:
    print(f"{valor} {moeda_origem} equivalem a {resultado} {moeda_destino}")
else:
    print("Moeda não suportada ou incorreta.")
