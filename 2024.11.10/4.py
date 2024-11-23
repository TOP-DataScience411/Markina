def countable_nouns(number: int, forms: tuple[str, str, str]) -> str:
    if not isinstance(number, int):
        raise ValueError("Первый аргумент должен быть целым числом.")
    if not isinstance(forms, tuple) or len(forms) != 3:
        raise ValueError("Второй аргумент должен быть кортежем из трёх строк.")
    
    if 11 <= number % 100 <= 14:
        return forms[2]  
    elif number % 10 == 1:
        return forms[0]  
    elif number % 10 in (2, 3, 4):
        return forms[1]  
    else:
        return forms[2]
        
        
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>>