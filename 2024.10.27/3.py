# запрашиваем ввод временного интервала
t_min = int(input("Введите временной интервал в минутах: "))
# Вычисляем часы и минуты
hours = t_min // 60
minutes = t_min % 60
# Выводим результат
print(f"{t_min} минут это {hours} час и {minutes} минут.")




# >
# >>> t_min = int(input("Введите временной интервал в минутах: "))
# Введите временной интервал в минутах: 150
# >>> hours = t_min // 60
# >>> minutes = t_min % 60
# >>> print(f"{t_min} минут это {hours} часов и {minutes} минут.")
# 150 минут это 2 час и 30 минут.