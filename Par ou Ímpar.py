número = int(input('Me diga qualquer número: '))
resultado = número % 2
if número == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é ÍMPAR.'.format(número))