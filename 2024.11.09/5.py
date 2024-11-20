from ref5 import scores_letters

word = input("Введите слово: ").upper().replace('Ё', 'Е')

one_letter = {letter: score for score, letters in scores_letters.items() for letter in letters}

score = sum(one_letter.get(letter, 0) for letter in word)

print("Количество символов: ", score)



#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 5.py
#Введите слово: кинематография
#Количество символов:  27