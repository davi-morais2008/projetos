from funcoes import lista_tarefas, lista_concluidas, add_tarefa, remov_tarefa, exibir_tarefas, concluir_tarefa, salvar_lista, exibir_menu


while True:
    salvar_lista()
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
