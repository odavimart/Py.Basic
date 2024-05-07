preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] À vista (Dinheiro/Cheque)
[2] À vista (Cartão)
[3] 2x no Cartão
[4] 3x ou mais''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção ==2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('A sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opção ==4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total /totparc
    print('A sua compra será parcelada em {}x no valor de R${:.S2} com juros.'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida. Tente novamente!')
print('A sua compra de R${:.2f}, vai passar a custar R${:.2f}.'.format(preço, total))