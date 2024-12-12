# #keys:Возвращает все ключи словаря.

# my_dict = {'name':'Rahma','age':14,'city':'Bishkek'}
# all_keys = my_dict.keys()
# print(all_keys)

# #values(): Возращает все значение словаря.

# data = {'x': 10 ,'y':20 , 'z': 30}
# all_values = data.values()
# print(all_values)

# #items():Возврашает все пары ключ-значение словаря в виде кортежей.

# my_dict = {'name':'Rahma','age': 30,'city':'Spanish'}
# items = my_dict.items()
# print(items)

# #get(): Возврашает значение по ключу: если ключ отсутствует,
# #возвращает указанное значение по умольчанию

# person = {'name':'Rahma','age':14.5}
# age = person.get('age', 0)
# height = person.get('height',100 )
# print(age)
# print(height)

# #pop(): Удаляет элемент по ключу и возвращает его значение.

# data = {'a':1, 'b':2,'y':3}
# value_b = data.pop('b')
# print(data)

# #update(): Добавляет пары ключ-значение из другого словаря.

# my_dict = {'name':'Rahm','age':14}
# my_dict.update({'city':'Bishkek', 'gender':'female'})
# print(my_dict)

# #setdefault(): Устанавливает значение по ключу, если ключ отсутствует.

# user_info = {'name':'Rahma','age':14.5}
# user_info = ('city','unknown')
# print(user_info)


# person = {'name':'Rahmatullo','username':'Tashtemirov','age':14.5}
# value_b = person.pop('age')
# print(person)

# person1 = {'class':'junior','school':16,'age':14.5}
# person1.update({'sss':'nike'})
# print(person1)

# person = {'name':'Rahma','username':'TASHTEMIROV'}
# age = person.get('name', 0)
# height = person.get('username',100 )
# print(age)
# print(height)


# my_dict = {'name':'Rahm','age':14}
# my_dict.update({'city':'Bishkek', 'pr':'hi'})
# print(my_dict)

# my_dict1 = {'JAKE': 'clik', 'age': 14}
# value = my_dict1.pop('JAKE')
# my_dict1['billy'] = value
# print(my_dict1)

num = input("Введите слово: ")
result = num[1:]  
print("Результат:", result)

text = input("Введите строку: ")
result = text + "!"
print("Результат:", result)

text = input("Введите строку: ")
result = text[:3]
print("Первые три символа:", result)

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
result = string1 + string2
print("Объединённая строка:", result)

text = input("Введите строку: ")
result = text.replace(" ", "_")
print("Результат:", result)

