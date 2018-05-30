"""
O grande mestre de xadrez Kary Gasparov inventou um novo tipo de problema de xadrez:
dada a posição de uma dama em um tabuleiro de xadrez vazio (ou seja, um tabuleiro 8 × 8, com 64 casas),
de quantos movimentos, no mínimo, ela precisa para chegar em outra casa do tabuleiro?

Entrada
A entrada contém vários casos de teste. A primeira e única linha de cada caso de teste contém quatro inteiros
X1, Y1, X2 e Y2 (1 ≤ X1, Y1, X2, Y2 ≤ 8).
A dama começa na casa de coordenadas (X1, Y1), e a casa de destino é a casa de coordenadas(X2, Y2).
No tabuleiro, as colunas são numeradas da esquerda para a direita de 1 a 8 e as linhas de cima para baixo também de 1 a 8.
As coordenadas de uma casa na linha X e coluna Y são (X, Y ).

O final da entrada é indicado por uma linha contendo quatro zeros.

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo um número inteiro,
indicando o menor número de movimentos necessários para a dama chegar em sua casa de destino.

"""

inicio = input().split()
a = ([int(i) for i in inicio])
x1 = a.pop(0)
y1 = a.pop(0)
destino = input().split()
a = ([int(i) for i in destino])
x2 = a.pop(0)
y2 = a.pop(0)


matriz = [] # lista vazia
for i in range(0, 8):
    linha = [] # lista vazia
    for j in range(0, 8):
        linha.append('xxxx')
    matriz.append(linha)

matriz[x1-1][y1-1] = 'Dama'
matriz[x2-1][y2-1] = 'Dest'

#Apenas para uso didatico
cabecalho = []
for i in range(0, 8):
    cabecalho.append(' x{} '.format(i+1))

print(cabecalho)
for j in matriz:
    print(j)
