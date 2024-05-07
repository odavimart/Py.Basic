distância = float(input('Qual é a distância para a sua viagem: '))
print('Você estará prestes a fazer uma viagem de {:.0f}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('A sua passagem custará R${:.2f}.'.format(preço))