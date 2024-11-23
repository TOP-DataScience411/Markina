def taxi_cost(length:int, wait: int=0)-> int | None:
    if length < 0 or wait < 0:
       return None
    base_cost = int(80)
    if length == 0:
        costcancel = base_cost+(3*wait)
        return round(costcancel)
    costroute = length//150*6
    costwait = wait*3
    total = base_cost+costroute+costwait
    return round(total)
    
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.10>python -i 2.py
#>>> taxi_cost(1500)
#140
#>>> taxi_cost(0,5)
#95
#>>> taxi_cost(2560)
#182
#>>> taxi_cost(-300)
#>>>