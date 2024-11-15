def remove_punctuation(text):
    # Задаем строку с символами, которые считаем знаками препинания
    punctuation = '.,:;!?–—\'\"()*/'
    # Генераторное выражение для фильтрации текста
    cleaned_text = ''.join(char for char in text if char not in punctuation)
    return cleaned_text

if __name__ == "__main__":
    # Чтение строки из стандартного ввода
    input_text = input().strip()
    # Удаление знаков препинания
    output_text = remove_punctuation(input_text)
    # Вывод очищенного текста
    print(output_text)
    
    
#C:\Users\Админ\Scripts\Markina\2024.11.03>python 7.py
#Привет! Как самочувствие? Сегодня мимо проезжал автобус, на котором мы собирались ехать.
#Привет Как самочувствие Сегодня мимо проезжал автобус на котором мы собирались ехать