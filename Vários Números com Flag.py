n = s = 0
tentativas = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    tentativas += 1
print(f'O resultado da soma dos números foi {s}.',end= ' ')
print(f'Você obteve {tentativas} tentativas.')
