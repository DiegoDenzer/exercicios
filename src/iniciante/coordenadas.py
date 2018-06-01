"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto,
ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
  Q2  |  Q1
______|______x
   Q3 |   Q4
      |y
Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
Q4 = 4.5 -2.2
Q1 = 0.1 0.1
"""
entrada = input().split()
coordenadas = ([float(i) for i in entrada])

if coordenadas[0] == 0 and coordenadas[1] == 0:
    print('Origem')
elif coordenadas[0] == 0 and coordenadas[1] != 0:
    print('Eixo Y')
elif coordenadas[0] != 0 and coordenadas[1] == 0:
    print('Eixo X')
elif coordenadas[0] > 0:
    if coordenadas[1] > 0:
        print('Q1')
    else:
        print('Q4')
elif coordenadas[0] < 0:
    if coordenadas[1] > 0:
        print('Q2')
    else:
        print('Q3')
