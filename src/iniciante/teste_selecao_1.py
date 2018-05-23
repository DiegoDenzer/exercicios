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
# não é a maneira correta =(
a = t.pop(0)
b = t.pop(0)
c = t.pop(0)
d = t.pop(0)


if a % 2 == 0 and (c >= 0 and d >= 0) and b > c and d > a and (a+b) < (c+d):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
