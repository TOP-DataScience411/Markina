year = int(input('Введите год: '))
# Определяем является ли год високосным по нашим условиям 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Да")
else:
    print("нет")
    
    
    
    
    
    
#   >>> year = int(input('Введите год: '))
#Введите год: 2024
#>>> if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#...     print("Да")
#... else:
#...     print("нет")
#...
#Да
#>>>