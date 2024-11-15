MILES = 1.60934
# Ввод целой и дробной части миль
wh_miles = int(input("Введите целую часть миль: "))
de_miles = float(input("введите дробную часть миль: "))
# Объединение целой и дробной части
total = wh_miles + de_miles
# Преобразование в км
km = total * MILES
km_round = round(km,1)
# Вывод резудьтата
print(f"{total} миль = {km_round} км")

# >>
# >>>
# >>> MILES = 1.60934                   
# >>> wh_miles = int(input("Введите целую часть миль: "))
# Введите целую часть миль: 16
# >>> de_miles = float(input("введите дробную часть миль: "))
# введите дробную часть миль: 9
# >>> total = wh_miles + de_miles
# >>> km = total * MILES
# >>> km_round = round(km,1) 
# >>> print(f"{total} миль = {km_round} км")
# 25.0 миль = 40.2 км