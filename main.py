import utils # Importa as funções auxiliares do sistema

def registrar_operacao(lista_produtos, saida_produtos = False): # Função para registrar entradas e saidas no estoque
    opcao = 0 # Coleta qual produto o usuário escolheu
    produto_escolhido = "" # Nome do produto
    qtde_produto = 0
    data_entrada = ""
    responsavel = ""
    dados_operacao = {} # Dicionário em que os dados do produto serão agrupados para registrar no hitórico de entradas ou no de saídas

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

    # Armazena os dados do produto no dicionário `dados_operacao`
    dados_operacao['nome'] = produto_escolhido
    dados_operacao['qtde'] = qtde_produto
    dados_operacao['data'] = data_entrada
    if saida_produtos: # Caso for um registro de uma saída, é retornado também o nome de quem fez a operação
        dados_operacao['responsavel'] = responsavel
    # print(f'\n{entrada}')

    return dados_operacao

def entrada_produtos(): # Registro de entrada de produtos no estoque
    print("\n" * 50)
    utils.imprimir_titulo("Entrada de Produtos")
    entrada = registrar_operacao(estoque) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(entrada) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_entradas.append(entrada) # Armazena os dados da entrada na lista `historico_entradas`

        atualizar_estoque(entrada) # Atualiza o estoque
    print("\n" * 50)
    print("Entrada registrada com sucesso!\n")

def saida_produtos(): # Registro de saída de produtos no estoque
    print("\n" * 50)
    utils.imprimir_titulo("Saída de Produtos")
    saida = registrar_operacao(estoque, True) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(saida) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_saidas.append(saida) # Armazena os dados da entrada na lista `historico_entradas`

        atualizar_estoque(saida, True) # Atualiza o estoque
    print("\n" * 50)
    print("Saída registrada com sucesso!\n")

def atualizar_estoque(dados_operacao, saida = False): # Atualiza o estoque
    produto = dados_operacao['nome']
    qtde = dados_operacao['qtde']

    for p in estoque:
        if p['nome'] == produto: # Procura pelo produto que foi adicionado ou retirado do estoque
            if saida: # Verifica se ocorreu uma entrada ou uma saída do estoque antes de fazer a operação de somar ou subtrair a quantidade no estoque
                p['qtde'] = p['qtde'] - qtde
            else:
                p['qtde'] = p['qtde'] + qtde

def listar_historico_entradas(): # Lista o histórico de entradas
    print("\n" * 50)
    print("Histórico de Entradas:\n")
    i = 0
    for entrada in historico_entradas:
        print(f'{i + 1} - {entrada['nome']}; {entrada['qtde']}; {entrada['data']}.')
        i = i + 1
    print()

def listar_historico_saidas():
    print("\n" * 50)
    print("Histórico de Saídas:\n")
    i = 0
    for saida in historico_saidas:
        print(f'{i + 1} - {saida['nome']}; {saida['qtde']}; {saida['data']}; {saida['responsavel']}.')
        i = i + 1
    print()

# ========================================================== Função Principal ==========================================================

estoque = [
    {'nome': 'iPhone 17 Pro Max', 'qtde': 10},
    {'nome': 'Dell G15', 'qtde': 3},
    {'nome': 'AOC Hero 24G2 144Hz', 'qtde': 6},
    {'nome': 'Apple AirPods Pro', 'qtde': 15},
    {'nome': 'Apple Watch Series 8', 'qtde': 8},
] # Estoque com os dados de todos os produtos

historico_entradas = [] # Lista de todos os registros de entrada no estoque
historico_saidas = [] # Lista de todos os registros de saída no estoque
opcao = 0

while True:
    utils.imprimir_titulo("Controle de Estoque")

    for produto in estoque: # Lista todos os produtos com suas respectivas quantidades
        print(produto['nome'], " -----> ", produto['qtde'])
    
    print("\nDigite apenas o número da opção desejada:")
    print("0-Sair\n1-Registrar Entrada\n2-Registrar Saída\n3-Histórico de Entradas\n4-Histórico de Saídas")

    opcao = utils.validar_int(">> ", 0, 4) # Coleta a escolha do usuário, faz a validação e retorna para a variável `opcao`

    match(opcao): # Executa um bloco de código dependendo da escolha do usuário
        case 0:
            print("\nAté mais! Saindo do programa...")
            break
        case 1:
            entrada_produtos() # Registra a entrada de produtos e atualiza o estoque e o histórico de entradas atualizado
        case 2:
            saida_produtos() # Registra a saída de produtos e atualiza o estoque e o histórico de entradas atualizado
        case 3:
            if historico_entradas: # Verifica se o histórico de entradas não está vazio
                listar_historico_entradas()
            else:
                print("\n" * 50)
                print("\nO histórico de entradas ainda está vazio!\n")
        case 4:
            if historico_saidas:
                listar_historico_saidas()
            else:
                print("\n" * 50)
                print("\nO histórico de saídas ainda está vazio!\n")
