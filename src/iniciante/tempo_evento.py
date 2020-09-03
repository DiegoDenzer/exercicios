"""
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
"""
from datetime import datetime

dia_inicio = input('Dia ')
hora_inicio = input()
dia_fim = input('Dia ')
hora_fim = input()

data1 = dia_inicio + '/04/2020 - ' + hora_inicio
data2 = dia_fim + '/04/2020 - ' + hora_fim
datetime_format = "%d/%m/%Y - %H:%M:%S"
result = datetime.strptime(data1, datetime_format)
result2 = datetime.strptime(data2, datetime_format)

print(result)