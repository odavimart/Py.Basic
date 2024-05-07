opção = 0
while True:
    print('''    [ 1 ] SOMAR
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR''')
    opção =int(input('>>>>>> ESCOLHA UMA DAS OPÇÕES: '))
    print('-=' * 16)
    n = int(input('Digite um número: '))
    if n == 0:
        break
    for c in range (1, 11):
        if opção == 1:
            print(f'{n} + {c} = {n + 1}')
        elif opção == 2:
            print(f'{n} - {c} = {n - c}')
        elif opção == 3:
            print(f'{n} x {c} = {n * c}')
        elif opção == 4:
            print(f'{n} / {c} = {n / c:.0f}')
    print('-=' * 16)
    print('FINALIZANDO PROGRAMA... VOLTE SEMPRE!')