dict = {}

while True:
    try:
        m = input("Вводим элементы для словаря: ")
        if not m:
            break
        key, value = m.split(maxsplit = 1)
        dict[value] = key
    except ValueError:
        continue

search = input("Что найти в словаре? ")

try:
    print(dict[search])
except KeyError:
    print("! value error !")
    
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 4.py
#Вводим элементы для словаря: 1004 ER_CANT_CREATE_FILE
#Вводим элементы для словаря: 1005 ER_CANT_CREATE_TABLE
#Вводим элементы для словаря: 1006 ER_CANT_CREATE_DB
#Вводим элементы для словаря: 1007 ER_DB_CREATE_EXISTS
#Вводим элементы для словаря: 1008 ER_DB_DROP_EXISTS
#Вводим элементы для словаря:
#Что найти в словаре? ER_CANT_CREATE_DB
#1006
#
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 4.py
#Вводим элементы для словаря: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#Вводим элементы для словаря: 4108 ER_GIPK_COLUMN_EXISTS
#Вводим элементы для словаря: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#Вводим элементы для словаря:
#Что найти в словаре? ER_CANT_OPEN_FILE
#! value error !
#>>>