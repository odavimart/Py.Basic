nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {} e {} a média do aluno é de {}.'.format(nota1, nota2, média))
if média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO!')
elif média >= 5 and média < 6.9:
    print('O aluno está REPROVADO!')
else:
    print('O aluno está APROVADO!')