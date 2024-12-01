def deck():
    suits = ['черви', 'бубны', 'пики', 'трефы']
    nominals = range(2, 15)
    for suit in suits:
        for nominal in nominals:
            yield (nominal,suit)




#C:\Users\Админ\Scripts\Markina\2024.11.24>python -i 1.py
#>>> list(deck())[::13]
#[(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]