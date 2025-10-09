import utils # Importa as funções auxiliares

# ========================================================== Funcionalidades ==========================================================

def registrar_entrada(lista_produtos): # Função para registrar entradas no estoque
    opcao = 0 # Coleta qual produto o usuário escolheu
    produto_escolhido = "" # Nome do produto
    qtde_produto = 0
    data_entrada = ""
    entrada = {} # Dicionário em que os dados do produto serão agrupados

    print(12 * "=" + " Entrada de Produtos " + 12 * "=" + "\n")

    print("Digite apenas o número da opção desejada:")
    print("(Ou digite \"0\" à qualquer momento para cancelar)\n")
    for i in range(len(lista_produtos)): # Lista todos os produtos que estão na lista `lista_produtos`
        print(f'{i + 1} - {lista_produtos[i]['nome']}')

    opcao = utils.validar_int(">> ", 0, len(lista_produtos)) # Valida a entrada do usuário, não permitindo que ele escolha uma opção inválida
    if opcao == 0: # Cancela o registro de produtos se o usuário digitar `0`
        print("Cancelando o registro...")
        return 0
    
    produto_escolhido = lista_produtos[opcao - 1]['nome'] # Recupera o nome do produto escolhido pelo usuário

    print(f'\n"{produto_escolhido}":')

    qtde_produto = utils.validar_int("Digite a quantidade: ", 0) # Valida a entrada do usuário, não permitindo que ele digite uma quantidade negativa
    if qtde_produto == 0: # Cancela o registro de produtos se o usuário digitar `0`
        print("Cancelando o registro...")
        return 0
    
    data_entrada = utils.validar_string("Digite a data de entrada (dd/mm/aaaa): ") # Valida a entrada do usuário, não permitindo a entrada de um valor inválido
    if data_entrada == "0": # Cancela o registro de produtos se o usuário digitar `0`
        print("Cancelando o registro...")
        return 0

    # Armazena os dados do produto no dicionário `entrada`
    entrada['nome'] = produto_escolhido
    entrada['qtde'] = qtde_produto
    entrada['data'] = data_entrada
    # print(f'\n{entrada}')

    return entrada
