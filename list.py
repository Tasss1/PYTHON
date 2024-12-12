# #append(): Добавляет элемент в конец списка

# my_list = [1, 2, 3, 4]
# my_list.append(4)
# print(my_list)

# #insert(): Вставляет элемент по указанному индексу

# numbers = [1, 2, 3]
# numbers.insert(0, 10)
# print(numbers)

# #index(): Возвращает индекс первого вхождения элемента в списке

# fruits = ['яблоко','груща','апельсин']
# index_pear = fruits.index('груща')
# print(index_pear)

# #sort(): Сортирует элементы в списке

# numbers = [2, 4 ,5 ,1 ,3 ,6 , 7 ,8]
# numbers.sort()
# print(numbers)

# #Шаг среза (взятие каждого второго элемента)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sliced_numbers = numbers [1:2:8]
# print(sliced_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del numbers [1]
# print(numbers)

# fruits = ['яблоко','груша','апельсин']
# fruits.append('apple')
# print(fruits)

# num = [10, 20, 30, 40,50]
# print(num[-2:])

# list1 = [1,2,3,4]
# list2 = [5,6,7,8,9,10]
# combined_list = list1 + list2
# print(combined_list)

# list = ['яблоко','груша','apple']
# list[1] = 'hamster'
# print(list)


# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])           
# print(my_list)                       

# numbers = [10, 20, 30, 40]
# removed_item = numbers.pop(2)        
# print(numbers)                       
# print(removed_item)                  

# fruits = ['яблоко', 'банан', 'груша', 'банан']
# fruits.remove('банан')               
# print(fruits)                        

# names = ['Alice', 'Bob', 'Charlie']
# names.reverse()                      
# print(names)                         

# colors = ['red', 'blue', 'red', 'green', 'red']
# red_count = colors.count('red')      
# print(red_count)                     

# numbers = [1, 2, 3]
# numbers.clear()
# print(numbers)

# p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# p.reverse()
# print(p)


# p = [1, 2, 3, 67,5, 7, 56, 9, 10]
# p.sort(reverse=True)
# print(p)

my_list = [10, 20, 30, 40, 50]
my_list[1] = 200
my_list[3] = 400
print(my_list)

my_list = [1, 2, 3, 2, 4, 5, 4, 6, 5]
print(list(set(my_list)))

my_list = [100, 200, 300]
reversed_list = my_list[::-1]

print(my_list)
print(reversed_list)


my_list = [5, 10, 15, 20, 25, 30]
print(my_list.index(20))

