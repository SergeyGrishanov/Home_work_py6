# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list_1 = []

list_num = 20
for i in range(0, list_num):
    list_1.append(randint(-15, 15))
print(list_1)
max = 10
min = 5

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print('index =', i, end = '  ')