fruits = []

while True:
    fruit = input("Введите название фрукта: ")
    if not fruit:
        break
    fruits.append(fruit)
    
l = len(fruits)

if l == 2:
	d = fruits[0]
	print(d)
	
elif l == 3:
	b = ' и '.join(fruits[0:2])
	print(b)
	
else:
	c = ', '.join(fruits[0:(l-3)])
	d = ' и '.join(fruits[(l-3):(l-1)])
	print(c + ',',d)
    
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.09>python -i 2.py
#Введите название фрукта: Яблоко
#Введите название фрукта: Мандарин
#Введите название фрукта: Апельсин
#Введите название фрукта: Груша
#Введите название фрукта: Киви
#Введите название фрукта:
#Яблоко, Мандарин, Апельсин и Груша
 