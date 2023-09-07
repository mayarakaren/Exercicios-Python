#Pesquisa de Livros em uma Biblioteca

biblioteca = [] #dicionário vazio

def adicionar_livro(titulo, autor):
    livro = {"Título": titulo, "Autor": autor}
    biblioteca.append(livro) #adiciona o livro no dicionário

def listar_livros(): #traz os livros presente no dicionário
    for livro in biblioteca:
        print(f"Título: {livro['Título']}, Autor: {livro['Autor']}") 

def pesquisar_livro(titulo):
    for livro in biblioteca:
        if livro['Título'] == titulo:
            print(f"Livro encontrado - Título: {livro['Título']}, Autor: {livro['Autor']}")

while True:
    print("Opções:")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Pesquisar livro por título")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        adicionar_livro(titulo, autor)
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        titulo = input("Digite o título do livro a ser pesquisado: ")
        pesquisar_livro(titulo)
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
