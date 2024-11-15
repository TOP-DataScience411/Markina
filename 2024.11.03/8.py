def fibonacci_sequence(n):
    a, b = 1, 1  # Начальные значения последовательности
    result = []  # Список для хранения чисел Фибоначчи

    for _ in range(n):
        result.append(a)  # Добавляем текущее число в результат
        a, b = b, a + b  # Обновляем значения a и b

    return result

if __name__ == "__main__":
    n = int(input().strip())  # Читаем натуральное число n
    fib_sequence = fibonacci_sequence(n)  # Генерируем последовательность Фибоначчи
    print(" ".join(map(str, fib_sequence)))  # Выводим последовательность через пробел
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.03>python 8.py
#18
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584
