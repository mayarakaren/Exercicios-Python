#Sistema de Gerenciamento de Tarefas

lista_de_tarefas = []

def adicionar_tarefa(tarefa):
    lista_de_tarefas.append({"Tarefa": tarefa, "Concluída": False})

def listar_tarefas():
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        status = "Concluída" if tarefa["Concluída"] else "Pendente"
        print(f"{i}. {tarefa['Tarefa']} ({status})")

def marcar_concluida(indice):
    if 1 <= indice <= len(lista_de_tarefas):
        lista_de_tarefas[indice - 1]["Concluída"] = True

def remover_tarefa(indice):
    if 1 <= indice <= len(lista_de_tarefas):
        del lista_de_tarefas[indice - 1]

while True:
    print("Opções:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        listar_tarefas()
        indice = int(input("Digite o número da tarefa concluída: "))
        marcar_concluida(indice)
    elif opcao == '4':
        listar_tarefas()
        indice = int(input("Digite o número da tarefa a ser removida: "))
        remover_tarefa(indice)
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
