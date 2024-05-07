from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''ESCOLHA A SUA JOGADA:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(2)
print('KEN')
sleep(3)
print('POOOOO!!')
print('-=' * 15)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:
        print('JOGADOR VENCE!')
    if jogador ==2:
        print('COMPUTADOR VENCE!')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCE')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    if jogador == 1:
            print('COMPUTADOR VENCE!')
    if jogador == 2:
        print('EMPATE')
else:
    print('Opção inválida. Tente Novamente!')