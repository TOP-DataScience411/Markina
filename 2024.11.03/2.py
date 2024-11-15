num = int(input()) #введение чисел
positive = 0 # инициализируем переменную для суммы положительных чисел
for _ in range(num):
    number = int(input())
    if number > 0: # проверяем является число положительным
       positive += number
Print(positive)
 

#>>> num = int(input())
#>>> positive = 0
#>>> # Считываем n чисел
#>>> for _ in range(num):
#...     number = int(input())
#...     # Проверяем, является ли число положительным
#...     if number > 0:
#...         positive += number
#...
#3
#14
#6
#-8
#5
#-3
#
#>>> print(positive)
#28