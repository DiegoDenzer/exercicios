

def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) * n


while True:
  try:
      entrada = input().split()
      num = ([int(numero) for numero in entrada])
      soma = f(num[0])
      soma += f(num[1])
      print(soma)
  except EOFError:
    break

