import core # Importa as funções para a lógica principal do programa

# ========================================================== Função Principal ==========================================================

estoque = [
    {'nome': 'iPhone 17 Pro Max', 'qtde': 10},
    {'nome': 'Dell G15', 'qtde': 3},
    {'nome': 'AOC Hero 24G2 144Hz', 'qtde': 6},
    {'nome': 'Apple AirPods Pro', 'qtde': 15},
    {'nome': 'Apple Watch Series 8', 'qtde': 8},
] # Estoque com os dados de todos os produtos

historico_entradas = [] # Lista de todos os registros de entrada no estoque

def main():

    # Registro de entrada de produtos no estoque
    entrada = core.registrar_entrada(estoque) # Coleta o retorno da função `registrar_entrada`

    if type(entrada) == dict: # Verifica se o retorno da função `registrar_entrada` é um dicionário, visto que, quando o retorno for 0, deve-se cancelar o registro de entrada
        historico_entradas.append(entrada) # Armazena os dados da entrada na lista `historico_entradas`

        # Atualiza o estoque
        produto_entrada = entrada['nome'] 
        qtde_entrada = entrada['qtde']
        for produto in estoque:
            if produto['nome'] == produto_entrada:
                produto['qtde'] = produto['qtde'] + qtde_entrada

for i in range(1):
    main()
    print()

print(historico_entradas)
print()
print(estoque)
