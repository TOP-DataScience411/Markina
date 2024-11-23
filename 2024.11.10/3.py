def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list[float]:
    if not isinstance(numbers, list) or not all(isinstance(x, float) for x in numbers):
        raise ValueError("Параметр 'numbers' должен быть списком вещественных чисел.")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Параметр 'n' должен быть неотрицательным целым числом.")
    
    if copy:
        numbers = numbers.copy()
    
    if len(numbers) <= 2 * n:
        return []
    
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers


#C:\Users\Админ\Scripts\Markina\2024.11.10>python -i 3.py
#>>> sample = [1.0, 2.0, 3.0, 4.0]
#>>> sample_stripped = numbers_strip(sample)
#>>> print(sample_stripped)  # [2.0, 3.0]
#[2.0, 3.0]
#>>> print(sample is sample_stripped)
#True
#>>> sample = [10.0, 20.0, 30.0, 40.0, 50.0]
#>>> sample_stripped = numbers_strip(sample, 2, copy=True)
#>>> print(sample_stripped)  # [30.0]
#[30.0]
#>>> print(sample is sample_stripped)
#False
#>>>