dias = int(input('Rodou quantos dias: '))
km = float(input('Rodou quantos km: '))
dinheiro = (dias * 60) + (km * 1.0)
print('O total a pagar: R${:.2f}'.format(dinheiro))