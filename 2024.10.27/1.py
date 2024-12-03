import datetime
name1 = input(' введите имя: ')
name2 = input(' введите фамилию: ')
yaer_of_birth = int(input(' введите год рождения: '))
now_year = datetime.datetime.now().year
age = now_year - yaer_of_birth
print(name2, name1 + ",", age)

#C:\Users\Админ\Scripts\Markina\2024.10.27>python -i 1.py
# введите имя: Кристина
# введите фамилию: Маркина
# введите год рождения: 1995
#Маркина Кристина, 29

