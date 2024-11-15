def sum_tele(message):
    chars = len(message)
    
    cost = 30
    
    sum_cost = cost * chars
    
    rub = sum_cost // 100
    ost = sum_cost % 100
    
    return rub, ost

def main():
    message = input()
    
    rub, ost = sum_tele(message)
    print(f"{rub} руб. {ost} коп.")
    
main()

#C:\Users\Админ\Scripts\Markina\2024.11.03>python 5.py
#Привет.Как дела?
#4 руб. 80 коп.