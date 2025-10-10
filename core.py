import utils # Importa as funções auxiliares

# ========================================================== Funcionalidades ==========================================================
def registrar_operacao(lista_produtos, saida_produtos = False): # Função para registrar entradas e saidas no estoque
    opcao = 0 # Coleta qual produto o usuário escolheu
    produto_escolhido = "" # Nome do produto
    qtde_produto = 0
    data_entrada = ""
    responsavel = ""
    entrada = {} # Dicionário em que os dados do produto serão agrupados

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

    if saida_produtos: # Caso for um registro de uma saída, haverá uma quantidade máxima de produtos que podem sair do estoque
        qtde_maxima = lista_produtos[opcao - 1]['qtde']
        qtde_produto = utils.validar_int("Digite a quantidade: ", 0, qtde_maxima) # Valida a entrada do usuário, não permitindo que ele digite uma quantidade negativa ou acima da quantidade atual do produto no estoque
    else:
        qtde_produto = utils.validar_int("Digite a quantidade: ", 0) # Valida a entrada do usuário, não permitindo que ele digite uma quantidade negativa

    if qtde_produto == 0: # Cancela o registro de produtos se o usuário digitar `0`
        print("Cancelando o registro...")
        return 0
    
    data_entrada = utils.validar_string("Digite a data de entrada (dd/mm/aaaa): ") # Valida a entrada do usuário, não permitindo a entrada de um valor inválido
    if data_entrada == "0": # Cancela o registro de produtos se o usuário digitar `0`
        print("Cancelando o registro...")
        return 0
    
    if saida_produtos: # Caso for um registro de uma saída, é solicitado que o usuário informe o nome de quem fez a operação
        responsavel = utils.validar_string("Digite o nome do responsável pela operação: ")
        if responsavel == "0":
            print("Cancelando o registro...")
            return 0

    # Armazena os dados do produto no dicionário `entrada`
    entrada['nome'] = produto_escolhido
    entrada['qtde'] = qtde_produto
    entrada['data'] = data_entrada
    if saida_produtos: # Caso for um registro de uma saída, é retornado também o nome de quem fez a operação
        entrada['responsavel'] = responsavel
    # print(f'\n{entrada}')

    return entrada
