from typing import Dict

def central_tendency(first: float, second: float, *numbers: float) -> Dict[str, float]:
    all_numbers = [first, second] + list(numbers)
    
    sorted_numbers = sorted(all_numbers)
    
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
  
    arithmetic = sum(all_numbers) / len(all_numbers)

    product = 1.0
    for number in all_numbers:
        product *= number
    geometric = product ** (1 / len(all_numbers))

    harmonic = len(all_numbers) / sum(1 / number for number in all_numbers)

    return {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }
    
# C:\Users\Админ\Scripts\Markina\2024.11.10>python -i 5.py
#>>> central_tendency(1, 2, 3, 4)
#{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}