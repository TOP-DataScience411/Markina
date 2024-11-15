import datetime
name1 = input(' введите имя: ')
name2 = input(' введите фамилию: ')
yaer_of_birth = int(input(' введите год рождения: '))
now_year = datetime.datetime.now().year
age = now_year - yaer_of_birth
print('\n',"{} {}, {}".format(name2, name1, age))



# >>>
# >>> import datetime
# >>> name1 = input(' введите имя: ')
# введите имя: Иван
# >>> name2 = input(' введите фамилию: ')
# введите фамилию: Петров
# >>> yaer_of_birth = int(input(' введите год рождения: '))
# введите год рождения: 1995
# >>> w_year = datetime.datetime.now().year
# >>> age = now_year - yaer_of_birth
# >>> now_year = datetime.datetime.now().year
# >>> age = now_year - yaer_of_birth
# >>> print('\n',"{} {}, {}".format(name2, name1, age))


# Петров Иван, 29 
#