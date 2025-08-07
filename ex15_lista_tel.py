# Criar um dicionário para armazenar contatos telefônicos.
# A chave do dicionário é o nome do contato. Cada chave deve estar associada a um
# número de telefone.
# Apresentar um menu ao usuário e permitir as seguintes funções:

# 1 - Adicionar contato.
# 2 - Buscar contato por nome.
# 3 - Deletar por nome.
# 4 - Deletar por numero
# 5 - imprimir lista
# 0 - Sair

#agenda
#nome
#telefone

agenda = {}

#criando contato
def adicionar_contato():
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    agenda[nome] = telefone
    print(f"\nContato '{nome}' adicionado com sucesso.\n") #mensagem de ok

#BUSCANDO O CONTATO
def buscar_contato():
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"\nContato {nome} Numero:  {agenda[nome]}\n")
    else:
        print("\033[91m\nContato não encontrado.\n\033[0m")

def deletar_por_nome():
    nome = input("Digite o nome do contato que deseja deletar: ")
    if nome in agenda:
        del agenda[nome]
        print(f"\n Contato '{nome}' deletado.\n")
    else:
        print("\033[91m\nContato não encontrado.\n\033[0m")

def deletar_por_numero():
    numero = input("Digite o número que deseja deletar: ")
    for nome in list(agenda):  # Usar list() para evitar erro ao modificar o dicionário durante a iteração
        if agenda[nome] == numero:
            del agenda[nome]
            print(f"\n Contato com número '{numero}' deletado.\n")
            return
    print("\033[91m\nNúmero não encontrado.\n\033[0m")


def imprimir_lista():
    if agenda:
        print("\n Lista de contatos:")
        for nome, numero in agenda.items():
            print(f"{nome}: {numero}")
    else:
        print("\033[91m\nNenhum contato cadastrado.\n\033[0m")

    print()

# Menu principal
while True:
    print("===== AGENDA TELEFÔNICA =====")
    print("1 - Adicionar contato")
    print("2 - Buscar contato por nome")
    print("3 - Deletar por nome")
    print("4 - Deletar por número")
    print("5 - Imprimir lista de contatos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        deletar_por_nome()
    elif opcao == "4":
        deletar_por_numero()
    elif opcao == "5":
        imprimir_lista()
    elif opcao == "0":
        print("\nSaindo da agenda. Até mais!")
        break
    else:
        print("\033[91m\nOpção inválida. Tente novamente.\033[0m")




