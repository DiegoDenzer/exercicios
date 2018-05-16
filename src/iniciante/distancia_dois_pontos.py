"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2)
e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1
e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída  1 7 5 9  = 4.4721
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""

xy1 = input().split()
xy2 = input().split()
x_y = ([float(i) for i in xy1])
x_y2 = ([float(i) for i in xy2])
x1 = x_y.pop(0)
x2 = x_y2.pop(0)# Pode e deve ser melhorado
y1 = x_y.pop(0)
y2 = x_y2.pop(0)

num1 = (x2-x1) ** 2
num2 = (y2-y1) ** 2

fim = (num1 + num2) ** (1/2)

print("{:.4f}".format(fim))