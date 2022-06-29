from datetime import date

data1 = input("Digite uma data: ")
data2 = input("Digite uma data: ")
data01 = data1.split("/")
data02 = data2.split("/")

date1 = date(int(data01[2]), int(data01[1]), int(data01[0]))
date2 = date(int(data02[2]), int(data02[1]), int(data02[0]))
diferenca = (date2-date1).days
print(diferenca)