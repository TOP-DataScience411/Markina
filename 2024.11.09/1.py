em = input( 'Введите Ваш email: ')

a = em.find('@')
b = em.find( '.',a)

if a == -1 or b == -1:
    print('нет')
    
else:
    print('да')
    


#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 1.py
#Введите Ваш email: chris@yandex.ru
#да
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 1.py
#Введите Ваш email: chgtjgj.ru
#нет