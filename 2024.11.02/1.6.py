def can_king_move(start, end):
    # Разделяем координаты на буквы и цифры
    start_col, start_row = start[0], int(start[1])
    end_col, end_row = end[0], int(end[1])
    
    # Проверяем, находится ли конечная клетка в пределах одного хода
    if abs(ord(start_col) - ord(end_col)) <= 1 and abs(start_row - end_row) <= 1:
        return True
    return False

# Чтение входных данных
start = input().strip()
end = input().strip()

# Проверка хода короля и вывод результата
if can_king_move(start, end):
    print("да")
else:
    print("нет")
    
    
    
        
#       >>> def can_king_move(start, end):
#   ...     # Разделяем координаты на буквы и цифры
#   ...     start_col, start_row = start[0], int(start[1])
#   ...     end_col, end_row = end[0], int(end[1])
#   ...
#   ...     # Проверяем, находится ли конечная клетка в пределах одного хода
#   ...     if abs(ord(start_col) - ord(end_col)) <= 1 and abs(start_row - end_row) <= 1:
#   ...         return True
#   ...     return False
#   ...
#   >>> start = input().strip()
#  g3
#   >>> end = input().strip()
#   f2
#   >>> if can_king_move(start, end):
#   ...     print("да")
#  ... else:
#  ...     print("нет")
#   ...
#   да
#  >>> start = input().strip()
#  c6
#  >>> end = input().strip()
#  d4
#   >>> # Проверка хода короля и вывод результата
#  >>> if can_king_move(start, end):
#  ...     print("да")
# ... else:
#  ...     print("нет")
#  ...
#  нет