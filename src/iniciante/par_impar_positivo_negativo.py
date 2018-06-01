"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
-5
0
-3
-4
12
"""
lista = []
for i in range(0, 5):
    lista.append(int(input()))

par = 0
positivo = 0
negativo = 0

for num in lista:
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    if num % 2 == 0:
        par +=1


print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(len(lista) - par))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
