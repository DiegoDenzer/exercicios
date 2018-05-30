"""
1 - 4.00
2 - 4.50
3 - 5.00
4 - 2.00
5 - 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""
entrada = input().split()
lanche = [int(i) for i in entrada]
lanches = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

for key in lanches.keys():
    if key == lanche[0]:
        print('Total: R$ {:.2f}'.format(lanche[1] * lanches.get(key)))