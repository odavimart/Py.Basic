from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,7):
    ano = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior = totmaior + 1
    elif idade < 21:
       totmenor = totmenor + 1
print('Existem {} pessoas de maioridade.'.format(totmaior))
print('Existem {} pessoas que ainda não possuem a maioridade.'.format(totmenor))
