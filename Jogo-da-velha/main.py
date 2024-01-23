'''
Atividade: Jogo da velha
Curso: Ciência da computação
Turma 1/A
Disciplina: Programação de computadores
'''


''' Esse código foi criado a partir de uma atividade solicitada em sala de aula, onde é simulado com precisão o jogo Tic-Tac-Toe (Jogo da Velha).

Nesse programa é necessário jogar com o "X" para vencer da máquina que utilizará o "O". 

Cada jogador terá seu turno para posicionar a letra em uma das casas. Vence aquele que fizer uma linha com 3 de sua respectiva letra, seja na vertical, horizontal ou diagonal.'''

import random as rd

#Variável para criar o tabuleiro com casas vazias.

casas = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']

#Função para mostrar o tabuleiro no console.

def criar_tabuleiro():
    print('=============')
    print('|',casas[0] , '|', casas[1], '|', casas[2], '|') 
    print('=============')
    print('|',casas[3] , '|', casas[4], '|', casas[5], '|')
    print('=============')
    print('|',casas[6] , '|', casas[7], '|', casas[8], '|')
    print('=============')  

#O bloco abaixo usa estrutura condicional para verificar se um jogador ganhou o jogo a partir das linhas horizontais, verticais ou diagonal.

def checar_vencedor(jogador):
    return ((casas[0] == jogador and casas[1] == jogador and casas[2] == jogador) or
            (casas[3] == jogador and casas[4] == jogador and casas[5] == jogador) or
            (casas[6] == jogador and casas[7] == jogador and casas[8] == jogador) or
            (casas[0] == jogador and casas[3] == jogador and casas[6] == jogador) or
            (casas[1] == jogador and casas[4] == jogador and casas[7] == jogador) or
            (casas[2] == jogador and casas[5] == jogador and casas[8] == jogador) or
            (casas[0] == jogador and casas[4] == jogador and casas[8] == jogador) or
            (casas[2] == jogador and casas[4] == jogador and casas[6] == jogador))

#Essa função realiza uma jogada lógica da IA e também verifica se a IA vence em uma jogada.

def jogada_logica(jogador):
    for i in range(9):
        if casas[i] == ' ':
            casas[i] = jogador
            if checar_vencedor(jogador):
                return i
            else:
                casas[i] = ' '

#Verifica se o jogador pode vencer na próxima jogada e bloqueia.
  
    if jogador == 'X':
        maquina = 'O'
    else:
        maquina = 'X'
    for i in range(9):
        if casas[i] == ' ':
            casas[i] = maquina
            if checar_vencedor(maquina):
                casas[i] = jogador
                return i
            else:
                casas[i] = ' '

#Função para realizar uma jogada aleatória.
  
    while True:
        jogada = rd.randint(0, 8)
        if casas[jogada] == ' ':
            return jogada
          
#Abaixo se encontra a função que realiza o loop do jogo.

jogando = True
while jogando: 
    jogada_valida = False
    while not jogada_valida:
        jogada = input('Digite a casa desejada (1-9): ')
        jogada = int(jogada) - 1
        if casas[jogada] == ' ':
            casas[jogada] = 'X'
            jogada_valida = True
        else:
            print('Movimento inválido, tente novamente.')
        criar_tabuleiro()
      
#Checar se o jogador venceu ou empatou.
      
        if checar_vencedor('X'):
            print('Você venceu!')
            jogando = False
        elif ' ' not in casas:
            print('Deu velha!')
            jogando = False
        if jogando:
            jogada_ia = jogada_logica('O')
            casas[jogada_ia] = 'O'
            print('A máquina escolheu a posição', jogada_ia+1)
            criar_tabuleiro()
        
#Checar se a IA empatou ou ganhou.
            if checar_vencedor('O'):
                print('A máquina venceu!')
                jogando = False
            elif ' ' not in casas:
                print('Deu velha!')
                jogando = False

'''
Referências:
      
Slides do blackboard
https://youtu.be/8cGzJ6oPD5Q
https://openai.com/blog/chatgpt
'''