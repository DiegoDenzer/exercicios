condicao = 1
entrada = []
while condicao < 21:
    x = int(input())
    entrada.append(x)
    condicao += 1

fim = list(reversed(entrada[10:20])) + list(reversed(entrada[20:10]))

for i, s in enumerate(fim):
    print(f'N[{i}] = {s}')