from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 7:
    print('''    [ 1 ] SOMAR
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] MAIOR
    [ 6 ] NOVO NÚMERO
    [ 7 ] SAIR DO PROGRAMA''')
    opção =int(input('>>>>>> ESCOLHA UMA DAS OPÇÕES: '))
    if opção == 1:
        print('Analisando dados...')
        sleep(0.5)
        soma = n1 + n2
        print('O resultado de {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        print('Analisando dados...')
        sleep(0.5)
        subtração = n1 - n2
        print('O resultado de {} - {} = {}'.format(n1, n2, subtração))
    elif opção == 3:
        print('Analisando dados...')
        sleep(0.5)
        multiplicação = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, multiplicação))
    elif opção == 4:
        print('Analisando dados...')
        sleep(0.5)
        divisão = n1 / n2
        print('O resultado de {} / {} = {:.0f}'.format(n1, n2, divisão))
    elif opção == 5:
        print('Analisando dados...')
        sleep(0.5)
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O resultado entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
       
    elif opção ==6:
        print('Informe os valores novamente. ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 7:
        print('Aguarde...')
        sleep(1)
        print('Finalizando...')
        sleep(1)
        print('Finalizado!')
    else:
        print('Dados inválidos. Tente novamente.')
print('=-='* 16)
print('FIM DO PROGRAMA. VOLTE SEMPRE!')      