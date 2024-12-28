from datetime import date, timedelta
from itertools import cycle

vacations = []

def schedule(start_date: date, first_weekday: int, *weekdays: int, total_days: int, date_format: str = '%d/%m/%Y'):
    if not (1 <= first_weekday <= 7) or any(not (1 <= wd <= 7) for wd in weekdays):
        raise ValueError("Дни недели должны быть в диапазоне от 1 до 7.")

    all_weekdays = [first_weekday] + list(weekdays)
 
    result = []
    current_date = start_date

    weekdays_cycle = cycle(all_weekdays)

    while len(result) < total_days:

        for weekday in weekdays_cycle:
            if len(result) >= total_days:
                break
        
            days_ahead = (weekday - current_date.isoweekday() + 7) % 7
            if days_ahead == 0: 
                days_ahead = 7
            
            current_date += timedelta(days=days_ahead)

            if any(start <= current_date < start + duration for start, duration in vacations):
                continue
            
            result.append(current_date.strftime(date_format))
    
    return result
    
#C:\Users\Админ\Scripts\Markina\2024.12.01>python -i 1.py
#>>> vacations = [
#...         (date(2023, 5, 1), timedelta(weeks=1)),
#...                 (date(2023, 7, 17), timedelta(weeks=1)),
#...                     ]
#>>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
#>>> print(len(py321))
#70
#>>> print(py321[28:32])
#['29/07/2023', '30/07/2023', '05/08/2023', '06/08/2023']