import core # Importa as funções para a lógica principal do programa
import utils

def entrada_produtos(): # Registro de entrada de produtos no estoque
    print("\n" * 50)
    utils.imprimir_titulo("Entrada de Produtos")
    entrada = core.registrar_operacao(estoque) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(entrada) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_entradas.append(entrada) # Armazena os dados da entrada na lista `historico_entradas`

        atualizar_estoque(entrada) # Atualiza o estoque
    print("\n" * 50)

def saida_produtos(): # Registro de saída de produtos no estoque
    print("\n" * 50)
    utils.imprimir_titulo("Saída de Produtos")
    saida = core.registrar_operacao(estoque, True) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(saida) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_saidas.append(saida) # Armazena os dados da entrada na lista `historico_entradas`

        atualizar_estoque(saida, True) # Atualiza o estoque
    print("\n" * 50)

def atualizar_estoque(dados_operacao, saida = False): # Atualiza o estoque
    produto = dados_operacao['nome']
    qtde = dados_operacao['qtde']

    for p in estoque:
        if p['nome'] == produto: # Procura pelo produto que foi adicionado ou retirado do estoque
            if saida: # Verifica se ocorreu uma entrada ou uma saída do estoque antes de fazer a operação de somar ou subtrair a quantidade no estoque
                p['qtde'] = p['qtde'] - qtde
            else:
                p['qtde'] = p['qtde'] + qtde

def main():
    opcao = 0

    while True:
        utils.imprimir_titulo("Controle de Estoque")

        for produto in estoque: # Lista todos os produtos com suas respectivas quantidades
            print(produto['nome'], " -----> ", produto['qtde'])
        
        print("\nDigite apenas o número da opção desejada:")
        print("0-Sair\t1-Registrar Entrada\t2-Registrar Saída")

        opcao = utils.validar_int(">> ", 0, 2) # Coleta a escolha do usuário, faz a validação e retorna para a variável `opcao`

        match(opcao): # Executa um bloco de código dependendo da escolha do usuário
            case 0:
                print("\nAté mais! Saindo do programa...")
                return 0
            case 1:
                entrada_produtos() # Registra a entrada de produtos e atualiza o estoque e o hitórico de entradas atualizado
            case 2:
                saida_produtos() # Registra a saída de produtos e atualiza o estoque e o hitórico de entradas atualizado

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

main()
