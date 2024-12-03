MILES = 1.60934
wh_miles = input("Введите целую часть миль: ")
de_miles = input("введите дробную часть миль: ")
total = float(wh_miles + "." + de_miles)
km = total * MILES
km_round = round(km,1)
print(f'{total} миль = {km_round} км')

#C:\Users\Админ\Scripts\Markina\2024.10.27>python -i 5.py
#Введите целую часть миль: 15
#введите дробную часть миль: 7
#15.7 миль = 25.3 км


