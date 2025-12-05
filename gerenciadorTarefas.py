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

