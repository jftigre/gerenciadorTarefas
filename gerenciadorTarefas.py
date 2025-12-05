def adicionar_tarefas(lista_tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    lista_tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def visualizar_tarefas(lista_tarefas):
    print("\nLista de Tarefas:")
    
    for i, tarefa in enumerate(lista_tarefas):
        numero_tarefa = i + 1
        status = "[✓]" if tarefa["completada"] else "[ ]"
        print(f"{numero_tarefa}. {tarefa['tarefa']} {status}")

def atualizar_tarefas(lista_tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa -= 1
    if indice_tarefa >= 0 and indice_tarefa < len(lista_tarefas):
        lista_tarefas[indice_tarefa]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa+1} atualizada para {novo_nome_tarefa}")
    else:
        print("Índice de tarefa inválido!")
    return


lista_tarefas = []

while True:
    print("\nMenu do Gerenciador de lista de tarefas:\n")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Concluir tarefa")
    print("5. Deletar tarefa")
    print("6. Sair\n")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_tarefa = str(input("Digite o nome da tarefa: "))
        adicionar_tarefas(lista_tarefas, nome_tarefa)

    elif escolha == 2:
        visualizar_tarefas(lista_tarefas)

    elif escolha == 3:
        visualizar_tarefas(lista_tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome_tarefa = str(input("Digite o novo nome da tarefa: "))
        atualizar_tarefas(lista_tarefas, indice_tarefa, novo_nome_tarefa)   
    