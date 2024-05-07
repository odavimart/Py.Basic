a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b > c:
    menor = b
if c < a and c > b:
    menor = c
menor = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor númerico é {}'.format(maior))
print('O menor valor número é {}'.format(menor))