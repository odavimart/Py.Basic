num = int(input('Informe um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTALMO
[3] HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para Octalmo é igual a {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Número inválido. Tente novamente!')