#lista de afazeres do davi zica lindogf
lista_tarefas = []
lista_concluidas = []

def add_tarefa():
    lista_tarefas.append(input("Digite a tarefa que deseje adcionar: ").upper())
    print("Tarefa adicionada.")
    pass

def remov_tarefa():
    while True:
        tarefa_removida = input('Digite a tarefa que deseje remover: ').upper()
        if tarefa_removida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        else:
            lista_tarefas.remove(tarefa_removida)
            print(f'A tarefa {tarefa_removida} foi removida de sua lista.')
            break

def exibir_tarefas():
    for x in lista_tarefas:
        if x not in lista_concluidas:
            print(f"[ ] {x}")
        else:
                print(f"[x] {x}")
    if len(lista_tarefas) == 0:
        print('Sua lista de tarefas está vazia.')
        pass

def concluir_tarefa():
    while True:
        tarefa_concluida = input('Digite a tarefa que deseje concluir: ').upper()
        if tarefa_concluida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        else:
            print(f'A tarefa {tarefa_concluida} foi marcada como concluída.')
            lista_concluidas.append(tarefa_concluida)
            break

def exibir_menu():
    print("""========================================
|       MENU - LISTA DE AFAZERES       |
========================================
|   [1] Adicionar tarefa               |
|   [2] Remover tarefa                 |
|   [3] Listar tarefas                 |
|   [4] Concluir Tarefas               |
|   [5] Sair                           |
========================================
    """)
    opcao = input("Digite sua escolha: ")
    return opcao
    
if __name__ == '__main__':
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            add_tarefa()

        elif opcao == '2':
            if len(lista_tarefas) == 0:
                print('Sua lista está vazia.')
            else:
                remov_tarefa()

        elif opcao == '3':
            print('Suas tarefas são:')
            exibir_tarefas()

        elif opcao == '4':
            if lista_tarefas == lista_concluidas:
                print("Todas as tarefas estão concluídas.")
            else:
                concluir_tarefa()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, digite novamente.")
