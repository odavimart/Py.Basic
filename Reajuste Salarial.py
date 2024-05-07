salário = float(input('Informe o salário do funcionário: '))
if salário >= 1280:
    novo = salário + (salário * 10 / 100)
else:
    novo = salário + (salário * 15 / 100)
print('Seu novo salário reajustado de {:.2f} vai para {:.2f}'.format(salário, novo))
