"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final,
mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.


"""
entrada = input().split()
numeros = ([int(numero) for numero in entrada])
inicio = [num for num in numeros]
def quickSort(lista, esquerda=None, direita=None):
    if esquerda is None:
        esquerda = 0
    if direita is None:
        direita = len(lista)-1

    if esquerda < direita:
        s = pivo(lista, esquerda, direita)
        quickSort(lista, esquerda, s-1)
        quickSort(lista, s+1, direita)


def pivo(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])
    (A[i+1], A[r]) = (A[r], A[i+1])
    return i+1

quickSort(numeros)

for num in numeros:
    print(num)
print("")
for n in inicio:
    print(n)