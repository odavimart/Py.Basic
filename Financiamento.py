casa = float(input('Informe o valor da casa: R$ '))
salário = float(input('Informe o salário: R$ '))
anos = int(input('Tempo de financiamento: '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.0F}, em {} anos, a prestação será de {:.0f}.'.format(casa, anos, prestação))
if prestação <= minimo:
    print('EMPRESTIMO CONCEDIDO!')
else:
    print('EMPRESTIMO NEGADO')