"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1,000,000).

Saída 576.73
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias.

"""
entrada = float(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0

while entrada >= 0.01:
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
        m1 += 1
        entrada -= 1
    if 1 > entrada >= 0.50:
        m2 += 1
        entrada -= 0.50
    if 0.50 > entrada >= 0.25:
        m3 += 1
        entrada -= 0.25
    if 0.25 > entrada >= 0.10:
        m4 += 1
        entrada -= 0.10
    if 0.10 > entrada >= 0.05:
        m5 += 1
        entrada -= 0.05
    if 0.05 > entrada >= 0.009:
        m6 += 1
        entrada -= 0.01

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(n100))
print("{} nota(s) de R$ 50.00".format(n50))
print("{} nota(s) de R$ 20.00".format(n20))
print("{} nota(s) de R$ 10.00".format(n10))
print("{} nota(s) de R$ 5.00".format(n5))
print("{} nota(s) de R$ 2.00".format(n2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(m1))
print("{} moeda(s) de R$ 0.50".format(m2))
print("{} moeda(s) de R$ 0.25".format(m3))
print("{} moeda(s) de R$ 0.10".format(m4))
print("{} moeda(s) de R$ 0.05".format(m5))
print("{} moeda(s) de R$ 0.01".format(m6))

