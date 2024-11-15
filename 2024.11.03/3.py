num = int(input())
print(sum([i for i in range(1, num + 1) if num % i == 0]))


#>>> num = int(input())
#50
#>>> print(sum([i for i in range(1, num + 1) if num % i == 0]))
#93