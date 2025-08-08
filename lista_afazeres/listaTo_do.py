lista_tarefas = []
lista_concluidas = []

ARQUIVO = "C:/Users/SENAI/Desktop/projetos/lista_afazeres/lista_tarefas.txt"

def salvar_arquivo():
    with open(ARQUIVO, "w") as f:
        for tarefa in lista_tarefas:
            if tarefa in lista_concluidas:
                f.write(f"[x] {tarefa}\n")
            else:
                f.write(f"[ ] {tarefa}\n")

def add_tarefa():
    tarefa = (input("Digite a tarefa que deseje adicionar: ").upper())
    if tarefa  not in lista_tarefas:
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada.")
    else:
        print("Está tarefa ja está na sua lista")
    salvar_arquivo()
    pass

def remov_tarefa():
    while True:
        tarefa_removida = input('Digite a tarefa que deseje remover: ').upper()
        if tarefa_removida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        else:
            lista_tarefas.remove(tarefa_removida)
            print(f'A tarefa {tarefa_removida} foi removida de sua lista.')
            salvar_arquivo()
            break

def exibir_tarefas():
    if not lista_tarefas:
        print('Sua lista de tarefas está vazia.')
        return

    print("\n========= SUA LISTA DE TAREFAS =========")
    for tarefa in lista_tarefas:
        if tarefa in lista_concluidas:
            status = "[x]"
        else:
            status = "[ ]"
        print(f"{status} {tarefa}")
    print("========================================")

def concluir_tarefa():
    while True:
        tarefa_concluida = input('Digite a tarefa que deseje concluir: ').upper()
        if tarefa_concluida not in lista_tarefas:
            print("Esta tarefa não está na sua lista.")
        else:
            print(f'A tarefa {tarefa_concluida} foi marcada como concluída.')
            lista_concluidas.append(tarefa_concluida)
            salvar_arquivo()
            break

def salvar_lista():
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                linha = linha.strip()       #esse strip arranca as quebra de linha 
                if linha.startswith("[x] "):
                    tarefa = linha[4:].strip()      
                    lista_tarefas.append(tarefa)
                    lista_concluidas.append(tarefa)
                elif linha.startswith("[ ] "):      #startswith ve se a string cmç com [ ]
                    tarefa = linha[4:].strip()      #aqui nesse caso aqui o strip vai remover os 4 primeiros caracteres
                    lista_tarefas.append(tarefa)
    except FileNotFoundError:
        with open(ARQUIVO, "a") as f:
            pass


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
    salvar_lista()
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
