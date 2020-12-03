"""Escreva um programa que leia três valores com ponto flutuante de dupla precisão:
A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor.
O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal."""

PI = 3.14159


# h.b /2
def area_triangulo(h , b):
    print("TRIANGULO: {:.3f}".format(h*b / 2))


# PI * raio²
def area_circulo(raio):
    print("CIRCULO: {:.3f}".format(PI * (raio **2)))


# (base+base) * altura / 2
def area_trapezio(b1, b2 , h):
    print("TRAPEZIO: {:.3f}".format(((b1+b2) * h / 2)))


# lado*lado
def area_quadrado(lado):
    print("QUADRADO: {:.3f}".format(lado*lado))


#
def area_retangulo(altura, base):
    print("RETANGULO: {:.3f}".format(altura * base))


valores = input().split()
abc = [float(i) for i in valores]

area_triangulo(abc[2], abc[0])
area_circulo(abc[2])
area_trapezio(abc[0], abc[1], abc[2])
area_quadrado(abc[1])
area_retangulo(abc[0], abc[1])
