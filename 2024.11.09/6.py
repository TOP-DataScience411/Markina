m = input("Введите двоичное число: ")

if m.startswith('0b'):
    m = m[2:]
elif m.startswith('b'):
    m = m[1:]

print("Да") if set(m) <= {'0', '1'} else print("Нет")


#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 6.py
#Введите двоичное число: 010101
#Да
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 6.py
#Введите двоичное число: 1b0101
#Нет
