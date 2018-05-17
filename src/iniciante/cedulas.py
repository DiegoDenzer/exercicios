"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1,000,000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias.

"""
entrada = 576
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while entrada != 0:
    if entrada >= 100:
        n100 += 1
        entrada -= 100
    if 100 > entrada >= 50:
        n50 += 1
        entrada -= 50
    if 50 > entrada >= 20:
        n20 += 1
        entrada -= 20
    if 20 > entrada >= 10:
        n10 += 1
        entrada -= 10
    if 10 > entrada >= 5:
        n5 += 1
        entrada -= 5
    if 5 > entrada >= 2:
        n2 += 1
        entrada -= 2
    if 2 > entrada >= 1:
        n1 += 1
        entrada -= 1

print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))
print("{} nota(s) de R$ 5,00".format(n5))
print("{} nota(s) de R$ 2,00".format(n2))
print("{} nota(s) de R$ 1,00".format(n1))
