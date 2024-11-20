seq1 = list(map(int, input("Первая последовательность чисел: ").split()))
seq2 = list(map(int, input("Вторая последовательность чисел: ").split()))

if len(seq2) != 0 and len(seq2) <= len(seq1):
    if seq2[0] in seq1:
        index = seq1.index(seq2[0])
        if seq1[index : index + len(seq2)] == seq2:
            print("Да")
        else:
            print("Нет")
elif len(seq2) == 0:
    print("Да")
else:
    print("Нет")
    
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 3.py
#Первая последовательность чисел: 1 2 3 5 8
#Вторая последовательность чисел: 3 5
#Да
#
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 3.py
#Первая последовательность чисел: 2 3 5
#Вторая последовательность чисел: 2 5
#Нет