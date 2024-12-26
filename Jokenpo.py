# JOGO DE JOKENPO - FAMOSO PEDRA, PAPEL, TESOURA

from random import randint

def jokenpo():
    saudacao()
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''
    JOKENPO TIME!
    Escolha uma opção:
    [ 0 ] - Pedra
    [ 1 ] - Papel 
    [ 2 ] - Tesoura\n''')
    
    while True:     # Válida a entrada do usuário
        try:        
            jogador = int(input('Qual a sua jogada? '))
            if jogador < 0 or jogador > 2:
                raise ValueError
            break
        except ValueError:
            print('Jogada inválida. Digite um número entre 0 e 2.')
            
    print('O Computador escolheu {}'.format(itens[computador]))
    print('O Player 1 escolheu {}'.format(itens[jogador]))

    if computador == 0:                     # COMPUTADOR JOGOU PEDRA
        if jogador == 0:                    # PEDRA
            print('Empatou!')
        elif jogador == 1:                  # PAPEL
            print('Jogador venceu!')
        elif jogador == 2:                  # TESOURA
            print('Vc Perdeu!')

    elif computador == 1:                   # COMPUTADOR JOGOU PAPEL
        if jogador == 0:                    # PEDRA
            print('Computador venceu!')
        elif jogador == 1:                  # PAPEL
            print('Empatou!')
        elif jogador == 2:                  # TESOURA
            print('Jogador Venceu!')
            
    elif computador == 2:                   # COMPUTADOR JOGOU TESOURA
        if jogador == 0:                    # PEDRA
            print('Jogador Venceu!')
        elif jogador == 1:                  # PAPEL
            print('Computador Venceu!')
        elif jogador == 2:                  # TESOURA
            print('Empatou!')
    else:
        print('Jogada Inválida!')
    
    again()

def again():
    executar_novo = input("Quer jogar novamente? [S] Sim ou [N] Não: \n")
    if executar_novo.upper().strip() in ['S', 'SIM']:
        jokenpo()
    elif executar_novo.upper().strip() in ['N', 'NÃO']:
        print("Até mais tarde!!!")
    else:
        again()
        
def saudacao():

    from datetime import datetime
   
    hora_primaria = int(datetime.now().strftime("%H"))

    if hora_primaria < 12:
        print('Bom dia')
    elif hora_primaria >= 12 or hora_primaria < 18:
        print('Boa tarde')
    elif hora_primaria >= 18 or hora_primaria < 24:
        print('Boa noite')

    
jokenpo()
