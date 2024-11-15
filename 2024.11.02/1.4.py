def get_color(cell):
    column = cell[0]  # Буква
    row = cell[1]     # Цифра

    # Преобразуем букву в номер (a=1, b=2, ..., h=8)
    column_index = ord(column) - ord('a') + 1
    row_index = int(row)

    # Определяем цвет клетки
    if (column_index + row_index) % 2 == 0:
        return "черный"
    else:
        return "белый"

# Чтение ввода
cell1 = input().strip()
cell2 = input().strip()

# Получаем цвета клеток
color1 = get_color(cell1)
color2 = get_color(cell2)

# Сравниваем цвета и выводим результат
if color1 == color2:
    print("да")
else:
    print("нет")
    
    
    
    
#      >>> def get_color(cell):
# ...     column = cell[0]  # Буква
#  ...     row = cell[1]     # Цифра
#  ...     column_index = ord(column) - ord('a') + 1
#  ...     row_index = int(row)
#  ...     if (column_index + row_index) % 2 == 0:
#  ...         return "черный"
#  ...     else:
#  ...         return "белый"
#  >>> cell1 = input().strip()
#  a1
#  >>> cell2 = input().strip()
#  b2
#  >>> color1 = get_color(cell1)
#  >>> color2 = get_color(cell2)
#  >>> if color1 == color2:
#  ...     print("да")
#  ... else:
#  ...     print("нет")
#  ...
# да