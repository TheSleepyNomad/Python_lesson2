"""
    2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

user_list = [] # Список, который пользователь заполняет сам

while True:
    print("Хотите добавить значение в список? Y/N:")
    user_choice = input("")

    if user_choice.lower() == "y":
        user_list.append(input("Введите новое значение: "))
    else:
        break


copy_list = user_list.copy()
# Проверяем длину списка
if len(user_list) % 2 == 0:
    for val in range(len(user_list)):
        if (val + 1) % 2 != 0:
            user_list[val] = user_list[val + 1]
        else:
            user_list[val] = copy_list[val - 1]
else:
    for val in range(len(user_list)):
        if user_list[val] == user_list[-1]:
            break
        elif (val + 1) % 2 != 0:
            user_list[val] = user_list[val + 1]
        else:
            user_list[val] = copy_list[val - 1]

print(f"Список, который был создан: {copy_list}")
print(f"Список, который был пересобран: {user_list}")
