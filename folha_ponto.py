from datetime import datetime
import calendar
import numpy as np

month = datetime.today().month
year = datetime.today().year
calendario = np.array(calendar.monthcalendar(year, month))

line = 0
column = 0

dias_uteis = []
dias_semana = []
dias_totais1 = []
dias_totais2 = []

dict_calendario = {}
dict_semana = {}


def mes_ano():
    if month == 1:
        month_name = "Janeiro"
    elif month == 2:
        month_name = "Fevereiro"
    elif month == 3:
        month_name = "Março"
    elif month == 4:
        month_name = "Abril"
    elif month == 5:
        month_name = "Maio"
    elif month == 6:
        month_name = "Junho"
    elif month == 7:
        month_name = "Julho"
    elif month == 8:
        month_name = "Agosto"
    elif month == 9:
        month_name = "Setembro"
    elif month == 10:
        month_name = "Outubro"
    elif month == 11:
        month_name = "Novembro"
    elif month == 12:
        month_name = "Dezembro"
    return month_name


def dia_semana():
    if column == 0:
        day = "Segunda-Feira"
    elif column == 1:
        day = "Terça-Feira"
    elif column == 2:
        day = "Quarta-Feira"
    elif column == 3:
        day = "Quinta-Feira"
    elif column == 4:
        day = "Sexta-Feira"
    return day


mes = mes_ano()

for item in range(0, 5):
    for item in range(0, 5):
        if calendario[line][column] != 0:
            dias_uteis.append(calendario[line][column])
            dias_semana.append(dia_semana())
        column += 1
    dias_totais1.append(dias_uteis)
    dias_totais2.append(dias_semana)
    dias_uteis = []
    dias_semana = []
    column = 0
    line += 1
dict_calendario[mes] = dias_totais1
line = 0

l = 0
for item in range(0, 5):
    for i, j in zip(dias_totais1[l], dias_totais2[l]):
        dict_semana[i] = j
    l += 1


print(dias_totais1)
print()
print(dias_totais2)
print()
print()
print(dict_calendario)
print()
print(dict_semana)
