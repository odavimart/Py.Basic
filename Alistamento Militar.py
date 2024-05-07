from datetime import date
atual = date.today().year
nasc = float(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {:.0f} tem {:.0f} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {:.0f} para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {:.0f} anos.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {:.0f} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {:.0f} anos.'.format(ano))
