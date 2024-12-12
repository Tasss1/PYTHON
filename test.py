# 1
# # Получаем строку от пользователя
# user_input = input('ведите строку: ')

# # Удаляем первый символ 

# result = user_input[1:]

# # Выводим результат
# print('Результат' , result)

# 2
# # Запрашиваем строку у пользователя
# input_str = input("Введите строку: ")

# # Добавляем к строке символ '!'
# result = input_str + "!"

# # Выводим результат
# print(result)

# # 3
# # Запрашиваем строку у пользователя
# input_str = input("Введите строку: ")

# # Получаем первые три символа с помощью среза
# first_three_chars = input_str[:3]

# # Выводим результат
# print(first_three_chars)



# # 4
# # Создаем две строки
# str1 = "Привет"
# str2 = "Мир"

# # Объединяем их в одну строку
# combined_str = str1 + " " + str2  # Добавляем пробел между словами

# # Заменяем символ в объединенной строке
# # Например, заменим букву "и" на "И"
# modified_str = combined_str.replace("и", "И")

# # Выводим результат
# print(modified_str)


# # 5
# # Запрашиваем строку у пользователя
# input_str = input("Введите строку: ")

# # Заменяем все пробелы на символ '_'
# modified_str = input_str.replace(" ", "_")

# # Выводим результат
# print(modified_str)
 


# # 1
# text = input("Введите строку: ")
# print("Верхний регистр:", text.upper())
# print("Нижний регистр:", text.lower())
# print(text)


# # 2
# text = "Python - это мощный язык программирования. Многие выбирают Python за его простоту и удобство."
# count_python = text.count("Python")
# print(count_python)
# print(text)

# # 3
# num = "Я учу Python"
# new_text = num.replace("Python", "программирование")
# print(new_text)
# print(num)


# # 4
# text = input("Введите строку: ")
# print(text[:5])
# print(text[-5:])
# print(text)


# # 5
# text = input("Введите слово: ")
# reversed_text = text[::-1]
# print(reversed_text)

# # 6
# a = [10,20,30]
# a.append(15)
# print(a)

# # 7
# a = [1,5,3,5,7,5]
# a.remove(5)
# print(a)

# # 8
# a = ['яблоко','банан','вишня','груша']
# a.index('вишня')
# print(a)

# # 9
# a = [8,3,5,2,1,9]
# a.sort()
# print(a)

# # 10

# ric = [2, 4, 6, 8, 10, 12, 14]
# elements = ric[0::2]  
# print(elements)



# num = True
# print(type(num))

# type --> это функция в Python, которая возврашает тип обьекта


# import random

# while (user := input("Камень, ножницы или бумага? (или 'выход'): ").lower()) != "выход":
#     comp = random.choice(["камень", "ножницы", "бумага"])
#     print(f"Компьютер: {comp}, Ты: {user}")
#     if user == comp:
#         print("Ничья!")
#     elif (user, comp) in [("камень", "ножницы"), ("ножницы", "бумага"), ("бумага", "камень")]:
#         print("Ты победил!")
#     else:
#         print("Компьютер победил!")
        


age = int(input('Сколько вам лет: '))

def age_years(age):
    return 2024-age
print(age_years(age))
    


