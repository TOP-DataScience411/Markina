def product(num):
    l = list(num)
    if not l:
        return 1.0
    return float (num[0]*product(num[1:]))
    
#C:\Users\Админ\Scripts\Markina\2024.11.24>python -i 2.py
#>>> product(range(10, 60, 10))
#12000000.0