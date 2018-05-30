"""
Leia 4 valores inteiros A, B, C e D.
A seguir,se B for maior do que C
e se D for maior do que A,
e a soma de C com D for maior que a soma de A e B e se C e D,
ambos, forem positivos e se a variável A for par
escrever a mensagem "Valores aceitos",
senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

"""
entrada = input().split()
t = ([float(i) for i in entrada])

d = {}
num = 0

for v in t:
    d[chr(97 + num)] = v
    num += 1

if d['a'] % 2 == 0 and (d['c'] >= 0 and d['d'] >= 0) and d['b'] > d['c'] and d['d'] > d['a'] \
        and (d['a'] + d['b']) < (d['c'] + d['d']):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
