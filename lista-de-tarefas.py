#Rayany e Luna - Lista de tarefas
lista_de_tarefas = [] 

def inserir_tarefas():
    tarefa = input("\n digite tarefa:")
    if tarefa == "":
        print("Tarefa não valida.")
        print("Digite outra!")
    else: 
        lista_de_tarefas.append(tarefa)
        print(f"\n Tarefa adicionada com sucesso!")
    voltar_para_o_menu()

def ver_tarefas():
    if lista_de_tarefas:
        for num, j in enumerate(lista_de_tarefas, start=1):
            print(f"{num}. {j}")
    else:
        print("Não possui tarefa!")
        voltar_para_o_menu()
    
def concluir_tarefa():
    try:
        ver_tarefas()
        concluir = int(input("Digite número da tarefa que deseja concluir: "))
        lista_de_tarefas.pop(concluir - 1)
        print("Tarefa retirada!")
    except(ValueError, IndexError):
        print("Opção inválida! ")

def substituir_tarefas():
    ver_tarefas()
    try:
        substituir = int(input("Digite o número da atrefa que deseje substituir: "))
        lista_de_tarefas[substituir - 1] = input("Digite uma nova tarefa: ")
        print(substituir)
        print("tarefa substituida, com sucesso!")
    except:
        print("Opção inválida!")
    

def excluir_tarefas():
    ver_tarefas()
    excluir = input("deseja escluir todas as tarefas? (sim/não) : ")
    if excluir == "sim":
        lista_de_tarefas.clear()
    elif excluir == "não" :
        return
    else:
       input("Poe favor escolha, sim/não:  ")

def menu():
    while True:
        print("\n ----------Lista de tarefas----------")
        print("1. Inserir tarefa")
        print("2. Ver tarefas")
        print("3. Concluir tarefa")
        print("4. Substituir tarefa")
        print("5. EXcluir todas tarefas")
        escolha = input("Digite o número desejado: ")

        if escolha == "1":
          inserir_tarefas()
        elif escolha == "2":
            ver_tarefas()
        elif escolha == "3":
            concluir_tarefa()
        elif escolha == "4":
            substituir_tarefas()
        elif escolha == "5":  
            excluir_tarefas() 
        else:
            print("Opção inválida!")


def voltar_para_o_menu():
    voltar = input("Digite sim ou não se quer voltar para o menu: ")
    if voltar == "sim":
        menu()
    elif voltar == "não":
        print("progama encerrado!")
    else:
        print("Opção inválida")
        voltar_para_o_menu()

menu()