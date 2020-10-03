"""
    4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_text = input("Введите строку: ")
print("Введеная строка:",user_text)

split_text = user_text.split(" ")
for num, value in enumerate(split_text, 1):
    print(f"{num}. {value}") if len(value) <= 10 else print(f"{num}. {value[0:10]}")
