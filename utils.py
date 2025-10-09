# ========================================================== Funções Auxiliares ==========================================================

def validar_int(label, min, max = 99999999999999999): # Valida a entrada de números inteiros
    while True:
        try:
            valor = int(input(label))
            while valor < min or valor > max: # Enquanto o valor não estiver entre o mínimo e o máximo, a entrada será solicitada novamente
                valor = int(input("Valor inválido! Tente novamente: "))
            break # Finaliza a execução do loop quando a tentativa for bem-sucedida
        except ValueError: # Volta ao início do loop quando ocorre `ValueError`
            print("Valor inválido! Tente novamente.")
            continue 
        except: # Volta ao início do loop quando ocorre algum outro tipo de erro
            print("Ocorreu algum erro! Tente novamente.")
            continue
    return valor # Retorna o valor de entrada validado

def validar_string(label):
    while True:
        try:
            valor = input(label)
            break # Finaliza a execução do loop quando a tentativa for bem-sucedida
        except ValueError:
            print("Valor Inválido! Tente novamente.")
            continue # Volta ao início do loop quando ocorre `ValueError`
        except:
            print("Ocorreu algum erro! Tente novamente.")
            continue # Volta ao início do loop quando ocorre algum outro tipo de erro
    return valor # Retorna o valor de entrada validado
