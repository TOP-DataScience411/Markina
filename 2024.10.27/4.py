number = int(input("Введите трехзначное число: "))
hund = number // 100
tens = (number // 10) % 10
un = number % 10
num = hund + tens + un
count = hund * tens * un
print(f'Сумма цифр = {num}\nПроизведение цифр = {count}')

#C:\Users\Админ\Scripts\Markina\2024.10.27>python -i 4.py
#Введите трехзначное число: 333
#Сумма цифр = 9
#Произведение цифр = 27






