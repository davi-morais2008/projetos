# Lista de afazeres do Davi Zica Lindogfuyu
lista_tarefas = []
lista_concluidas = []

ARQUIVO = "C:/Users/SENAI/Desktop/projetos/lista_tarefas.txt"

def salvar_em_arquivo():
    with open(ARQUIVO, "w") as f:
        for tarefa in lista_tarefas:
            if tarefa in lista_concluidas:
                f.write(f"[x] {tarefa}\n")
            else:
                f.write(f"[ ] {tarefa}\n")

def add_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ").upper()
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada.")
    salvar_em_arquivo()

def remov_tarefa():
    while True:
        tarefa_removida = input('Digite a tarefa que deseja remover: ').upper()
        if tarefa_removida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        else:
            lista_tarefas.remove(tarefa_removida)
            if tarefa_removida in lista_concluidas:
                lista_concluidas.remove(tarefa_removida)
            print(f'A tarefa {tarefa_removida} foi removida de sua lista.')
            salvar_em_arquivo()
            break

def exibir_tarefas():
    cont = 0
    for x in lista_tarefas:
        if x in lista_concluidas:
            print(f"{cont}[x] {x}")
        else:
            print(f"{cont}[ ] {x}")
        cont += 1
    if len(lista_tarefas) == 0:
        print('Sua lista de tarefas está vazia.')

def concluir_tarefa():
    while True:
        tarefa_concluida = input('Digite a tarefa que deseja concluir: ').upper()
        if tarefa_concluida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        elif tarefa_concluida in lista_concluidas:
            print("Essa tarefa já foi concluída.")
        else:
            lista_concluidas.append(tarefa_concluida)
            print(f'A tarefa {tarefa_concluida} foi marcada como concluída.')
            salvar_em_arquivo()
            break

def exibir_menu():
    print("""========================================
|       MENU - LISTA DE AFAZERES       |
========================================
|   [1] Adicionar tarefa               |
|   [2] Remover tarefa                 |
|   [3] Listar tarefas                 |
|   [4] Concluir tarefa                |
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
            if len(lista_tarefas) == 0:
                print("Sua lista está vazia.")
            elif len(lista_tarefas) == len(lista_concluidas):
                print("Todas as tarefas estão concluídas.")
            else:
                concluir_tarefa()

        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, digite novamente.")
