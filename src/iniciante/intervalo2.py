


qtd = int(input())
dentro = []
fora = []
for _ in range(qtd):
    valor = int(input())
    if 20 >= valor >= 10:
        dentro.append(valor)
    else:
        fora.append(valor)

print('{} in'.format(len(dentro)))
print('{} out'.format(len(fora)))
