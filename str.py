# #типы данных
# int
# float
# bool
# str

# # upper(): Преобразует все символы строки в верхний регистр.

# text = 'Привет, мир!'
# upper_text = text.upper()      #uppper_text = 'ПРИВЕТ, МИР!'
# print(upper_text)

# # lower(): Преобразует все символы строки в нижний регистр.

# message = 'Python'
# lower_message = message.lower() # lower_message = 'python'

# #count(): Возврашает количество вхождений подстроки в строке.

# sentence = 'Python - прекрасный язык програмирования, Python!'
# count_python = sentence.count('Python')

# #replace(): Заменяет все вхождения одной подстроки на другую.

# pharase = 'Я люблю Python'
# updated_pharase = pharase.replace('Python','програмирование')

# a = input('ведите текст')
# print(a.capitalize())


# # Примеры различных типов данных
# coordinates = (40.7128, 74.0060)  # Кортеж (Tuple)
# unique_numbers = {1, 2, 3, 4, 5}  # Множество (Set)
# person = {"name": "Рахма", "age": 25, "city": "Москва"}  # Словарь (Dictionary)
# nothing = None  # NoneType
# complex_number = 3 + 5  # Комплексное число (Complex)

# # Вывод типов данных и их значений
# print("Координаты:", coordinates, "- Тип:", type(coordinates))
# print("Уникальные числа:", unique_numbers, "- Тип:", type(unique_numbers))
# print("Персональные данные:", person, "- Тип:", type(person))
# print("Пустое значение:", nothing, "- Тип:", type(nothing))
# print("Комплексное число:", complex_number, "- Тип:", type(complex_number))




txt = "banana"

x1 = txt.islower()
x2 = txt.isupper()
x3 = txt.isdigit()
x4 = txt.startswith("ba")
x5 = txt.endswith("a")

print(x1)  # Проверяет, состоит ли строка из строчных букв
print(x2)  # Проверяет, состоит ли строка из заглавных букв
print(x3)  # Проверяет, состоит ли строка только из цифр
print(x4)  # Проверяет, начинается ли строка с "ba"
print(x5)  # Проверяет, заканчивается ли строка на "na"