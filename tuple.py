''''Кортежи (tuple)

Упорядоченные неизменяемые последовательности 
Примеры...'''

#count(): Возврашает количество вхождений элемента в кортеже.

my_count = (1,2,3,4,5,5)
count1 = my_count.count(5)
print(count1)

#index(): Возвращает индекс первого вхождения элемента в кортеже

items = ('apple','banana','apple','orange')
index_banana = items.index('banana')
print(index_banana)

#len(): Возвращает длину кортежа

fruits = ('apple','banana','orange')
lenght = fruits.__len__()
print(lenght)