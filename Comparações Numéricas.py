from time import sleep
valor1 = int(input('Informe o primeiro número:'))
valor2 = int(input('Informe o segundo número: '))
if valor1 > valor2:
    print('ANALISANDO...')
    sleep(2)
    print('O primeiro número é maior')
elif valor2 > valor1:
    print('ANALISANDO...')
    sleep(2)
    print('O segundo número é maior')
elif valor1 == valor2:
    print('ANALISANDO...')
    sleep(2)
    print('Números correspondem ao mesmo valor, são iguais.')

print('Tente novamente.')