files = input("Введите имена файлов: ").split("; ")

count = {}
rename = []

for name in files:
    if name not in count:
        count[name] = 1
        rename.append(name)
    else:
        count[name] += 1
        dot_index = name.find('.')
        if dot_index != -1:
            new = f"{name[:dot_index]}_{count[name]}{name[dot_index:]}"
            rename.append(new)
        else:
            rename.append(name)

rename.sort()

for name in rename:
    print(name)
    
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 8.py
#Введите имена файлов: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
#1.py
#1_2.py
#1_3.py
#aux.h
#functions.h
#main.cpp
#main_2.cpp
#main_3.cpp
#src.tar.gz
#src_2.tar.gz