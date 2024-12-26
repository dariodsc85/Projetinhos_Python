# Tabuada em Python |Dário Costa| ** Atualizada em 25/05/23 ** 

import os

def tabuada():
    while True:
        os.system('cls')
        num = input("Informe um número para a Tabuada: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Valor inválido. Digite um número inteiro válido.")
    
    for c in range(1, 11):                                  # range de 1 até 10 / O ultimo é sempre ignorado pelo sistema
        print('{} X {} = {}'.format(num, c, num*c))         # O print vai ser repetido até o comando FOR se atendido
    
    again()    
        
def again():
    import os   # import para a usar o cls / Limpar a tela
    calcular_denovo = input("Quer calcular novamente: [S] Sim ou [N] Não: \n")
    if calcular_denovo.upper().strip()[0] == "S":
        os.system('cls')    # Usado no import
        tabuada()
    elif calcular_denovo.upper().strip()[0] == "N":
        os.system('cls')
        print("Encerrando...")
    else:
        print('Valor invalido!')
        again()
    # fim da função again

tabuada()
