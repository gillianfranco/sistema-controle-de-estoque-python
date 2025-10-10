import core # Importa as funções para a lógica principal do programa
import utils

def entrada_produtos():
    # Registro de entrada de produtos no estoque
    utils.imprimir_titulo("Entrada de Produtos")
    entrada = core.registrar_operacao(estoque) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(entrada) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        core.historico_entradas.append(entrada) # Armazena os dados da entrada na lista `historico_entradas`

        # Atualiza o estoque
        produto_entrada = entrada['nome'] 
        qtde_entrada = entrada['qtde']
        for produto in estoque:
            if produto['nome'] == produto_entrada:
                produto['qtde'] = produto['qtde'] + qtde_entrada

def saida_produtos():
    # Registro de entrada de produtos no estoque
    utils.imprimir_titulo("Saída de Produtos")
    saida = core.registrar_operacao(estoque, True) # Solicita as informações sobre o registro ao usuário e coleta o retorno da função

    if type(saida) == dict: # Verifica se o retorno da função `registrar` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_saidas.append(saida) # Armazena os dados da entrada na lista `historico_entradas`

        # Atualiza o estoque
        produto_saida = saida['nome'] 
        qtde_saida = saida['qtde']
        for produto in estoque:
            if produto['nome'] == produto_saida:
                produto['qtde'] = produto['qtde'] - qtde_saida

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

def main():
    # entrada_produtos()
    saida_produtos()


for i in range(1):
    main()
    print()

print(historico_entradas)
print()
print(estoque)
