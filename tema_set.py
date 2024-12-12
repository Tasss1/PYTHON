# a = {1,2,3,1,2,3,1,2,3}
# b = {'lik','lok','lik','lok','lik','lok'}
# print(b)

# my_set = {1, 2, 3, 4, 4}
# print(my_set)  


# # методы

# # ДОБАВЛЕНИЕ:

# # add()
# # Добавляет элемент в множество.

# my_set = {1, 2, 3}
# my_set.add(4) 
# print(my_set)


# # УДАЛЯЕМЫЕ МЕТОДЫ:

# # remove()
# # Удаляет элемент. Ошибка, если элемента нет.

# my_set = {1, 2, 3}
# my_set.remove(2) 
# print(my_set)

# # discard()
# # Удаляет элемент, если он существует. Ошибки не возникает.

# my_set = {1, 2, 3}
# my_set.discard(2)
# print(my_set)

# # pop()
# # Удаляет и возвращает произвольный элемент.

# my_set = {1, 2, 3}
# elem = my_set.pop()
# print(my_set, elem)  

# # clear()
# # Очищает множество

# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)  



# # ОПЕРАЦИИ НАД МНОЖЕТЕЛЯМИ:

# # union()
# # Возвращает объединение множеств.

# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a.union(b)
# print(result)


# # intersection()
# # Возвращает пересечение множеств.

# a = {1, 2, 3}
# b = {2, 3, 4}
# result = a.intersection(b)
# print(result) 

# # difference()
# # Возвращает разность множеств.

# a = {1, 2, 3}
# b = {2, 3, 4}
# result = a.difference(b)
# print(result)  

# # symmetric_difference()
# # Возвращает симметрическую разность.
# # True
# a = {1, 2, 3}
# b = {3, 4, 5}
# result = a.symmetric_difference(b)
# print(result) 


# # МЕТОДЫ ПРОВЕРКИ:

# # issubset()
# # Проверяет, является ли множество подмножеством.
# # True
# a = {1, 2}
# b = {1, 2, 3}
# print(a.issubset(b)) 

# # issuperset()
# # Проверяет, является ли множество надмножеством.
# # True
# a = {1, 2, 3}
# b = {1, 2}
# print(a.issuperset(b))  

# # isdisjoint()
# # Проверяет, не пересекаются ли множества.

# a = {1, 2}
# b = {3, 4}
# print(a.isdisjoint(b)) 

# # ОПЕРАЦИИ С ОБНОВЛЕНИЕ МНОЖЕСТВАМИ:

# # update()
# # Добавляет элементы из других множеств.

# a = {1, 2}
# b = {3, 4}
# a.update(b)
# print(a) 

# # intersection_update()
# # Оставляет только общие элементы.

# a = {1, 2, 3}
# b = {2, 3, 4}
# a.intersection_update(b)
# print(a) 

# # difference_update()
# # Удаляет элементы, которые есть в других множествах.

# a = {1, 2, 3}
# b = {2, 3, 4}
# a.difference_update(b)
# print(a) 

# # symmetric_difference_update()
# # Оставляет только элементы, которые не общие.

# a = {1, 2, 3}
# b = {3, 4, 5}
# a.symmetric_difference_update(b)
# print(a)  



# 1. Наглядно показывает плюсы и минусы set
# Преимущества set:
# ✅ Уникальность данных : автоматически удаляются дубликаты.
# ✅ Высокая производительность : операции проверки, добавления и удаления элементов выполняются быстрее, 
# чем в списках (за счет хеширования).
# ✅ Математические операции : простое объединение операций, международные операции и другие операции.
# Ограничение set:
# ❌ Неупорядоченность : нельзя обращаться к элементу по индексу.
# ❌ Только неизменяемые типы данных : нельзя добавить список или другое множество, 
# только неизменяемых объектов (например, числа, строки, кортежи).
# питон

# set – бул Python тилиндеги коллекциялык тип, анын өзгөчөлүгү кайталанган элементтерди сактабайт
#  жана элементтердин тартиби маанилүү эмес. set түрүнө төмөнкүлөр кире алат:

# Кире ала турган типтер:

# 1. Hashable объектилер (туруктуу, өзгөрүлбөс жана уникалдуу болууга тийиш). Мисалы:

# Сандар: int, float, complex

# Символдук саптар: str

# Туурактуу түрмөктөр (tuple): Туурактуу түрмөк ичинде дагы hashable элементтер болушу керек.

# Frozen sets: (туурактуу set түрү)




# Кире албай турган типтер:

# Кээ бир типтерди set түзүү үчүн колдонууга болбойт, анткени алар өзгөрүлмө (mutable)
#  болуп саналат жана hashable эмес:

# Тизме (list)

# Кадимки топтом (set)

# Сөздүк (dict)


# Мисал:

# # Hashable жана hashable эмес түрлөрдү текшерүү
# my_set = {1, 3.14, "hello", (1, 2, 3)}  # Мүмкүн
# print(my_set)

# # Төмөнкү аракет ката кетирет
# my_set = {1, [2, 3], {"a": 1}}  # TypeError: unhashable type

# Эгерде set менен иштегенде катаны болтурбоо керек болсо, hashable түрлөрдү гана колдонгула.