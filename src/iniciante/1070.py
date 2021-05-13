x = int(input())
aux = 0

if x % 2 != 0:
    print(x)
    aux += 1

while aux < 6:
    x += 1
    if x % 2 != 0:
        print(x)
        aux += 1

