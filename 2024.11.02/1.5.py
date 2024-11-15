def can_rook_move(start, end):
    # Разделяем координаты на буквы и цифры
    start_col, start_row = start[0], int(start[1])
    end_col, end_row = end[0], int(end[1])
    
    # Проверяем, совпадают ли колонки или строки
    return start_col == end_col or start_row == end_row

# Чтение входных данных
start_position = input().strip()
end_position = input().strip()

# Проверка и вывод результата
if can_rook_move(start_position, end_position):
    print("да")
else:
    print("нет")
    
    
    
#       >>> def can_rook_move(start, end):
#    ...     # Разделяем координаты на буквы и цифры
#   ...     start_col, start_row = start[0], int(start[1])
#   ...     end_col, end_row = end[0], int(end[1])
#   ...
#  ...     # Проверяем, совпадают ли колонки или строки
#  ...     return start_col == end_col or start_row == end_row
#  ...
#  >>> start_position = input().strip()
#  d4
#  >>> end_position = input().strip()
#  e4
#  >>> if can_rook_move(start_position, end_position):
# ...     print("да")
# ... else:
# ...     print("нет")
#  ...
#  да
#   >>> def can_rook_move(start, end):
#  ...     # Разделяем координаты на буквы и цифры
#   ...     start_col, start_row = start[0], int(start[1])
#   ...     end_col, end_row = end[0], int(end[1])
#   ...
#  ...     # Проверяем, совпадают ли колонки или строки
#  ...     return start_col == end_col or start_row == end_row
#  ...
#  >>> start_position = input().strip()
#  a2
#  >>> end_position = input().strip()
# c4
# >>> if can_rook_move(start_position, end_position):
# ...     print("да")
# ... else:
#  ...     print("нет")
#  ...
# нет
 