# Ввод трехзначногог числа
number = int(input("Введите трехзначное число: "))
# Проверка на трехзначность
if 100 <= number <= 999
hund = number // 100
tens = (number // 10) % 10
un = number % 10
# расчет суммы и произведения 
sum = hund + tens + un
count = hund * tens * un

# Вывод результата
print("Сумма цифр =", sum)
print("Произведение цифр =", count)
else:
print("Ошибка: Введите трехзначное положительное число.")


# >>>
# >>>
# >>> number = int(input("Введите трехзначное число: "))
# Введите трехзначное число: 333
# >>> hund = number // 100
# >>> tens = (number // 10) % 10
# >>> un = number % 10
# >>> sum = hund + tens + un
# >>> count = hund * tens * un
# >>> print("Сумма цифр =", sum)
# Сумма цифр = 9
# >>> print("Произведение цифр =", count)
# Произведение цифр = 27
#
#
