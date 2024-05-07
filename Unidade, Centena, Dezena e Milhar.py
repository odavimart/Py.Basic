n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade: {}'.format(u))
print('A dezena: {}'.format(d))
print('A centena: {}'.format(c))
print('O milhar: {}'.format(d))