print('=' * 25)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
print('=' * 25)
for c in range (primeiro, décimo + razão, razão):
    print('{}'.format(c), end= '-> ')
print('Acabou')