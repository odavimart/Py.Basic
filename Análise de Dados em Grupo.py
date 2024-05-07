tot18 = 0
toth = 0
totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
      sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 =+ 1
    if sexo == 'M':
        toth =+ 1
    if sexo == 'F' and idade <= 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
           break
print(f'O total de pessoas maior de 18: {tot18}.')
print(f'O total de homens cadastrados: {toth}.')
print(f'O total de mulheres com menos de 20 anos: {totm20}')