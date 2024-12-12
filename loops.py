# sib = int(input('Ведите слова'))
# for i in range(sib , 1 , -1):
#    print('i' *i)

# sib = int(input('Ведите слова: '))
# for i in range(1,11):
#  print('*' *10)

# sib = int(input('Ведите слова: '))
# for i in range(1, 1001):
#  print(f'{i} , {sib}')


# i = 0
# while i <= 101:
#  print(i)
#  i += 1

# for i in range(101):
#   print(i)

# for name in range(1,10):
#   print(name)

# sib = int(input('Ведите число: '))
# for i in range(sib):
#   print('*' *10)

# for i in range(1, 11):
#   print(i, '.    5')

# stop = int(input('Ведите слово stop: '))
# start = int(input('Ведите слово start: '))
# for i in range(start,stop,-1):
#       print('i' *i)


# while True:
    # print('$')

# i = 0 
# while i < 101:
#     i += 1
#     if i == 51:
#         break
#     print(i)

# i = 0 
# while i <100:
#      i += 1
#      if i == 3:
#         continue
#      print(i)


while True:
    print('Простой калькулятор')
    print('Доступные операции:')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Умножение')
    print('4. Деление')
    print('5. Выход')
    
    vybor = input('Выберите операцию (1/2/3/4/5): ')
    
    if vybor == '5':
        print('Выход из калькулятора')
        break  
    
    if vybor in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))
        except ValueError:
            print("Ошибка: пожалуйста, введите числовые значения.")
            continue

        if vybor == '1':
            result = num1 + num2
            print('Результат:', result)
        elif vybor == '2':
            result = num1 - num2
            print('Результат:', result)
        elif vybor == '3':
            result = num1 * num2
            print('Результат:', result)
        elif vybor == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно.")
            else:
                result = num1 / num2
                print('Результат:', result)
    else:
        print("Ошибка: выберите корректную операцию.")

# while True:
    # print('sorry')

# n = int(input('Введите число: '))  
# print(f'Таблица умножения для числа {n}:')  
# for i in range(1, 11): 
#     result = n * i  
#     print(f'{n} x {i} = {result}')  


# num = int(input('Ведите цифру: '))
# for i in range(num):
    #   print('*' *10)


# cart = []

# while True:
#     print('Здраствуйте это магазин одежды:')
#     print('Чтобы открыть меню нажмите на << 1 >>')
#     print('Чтобы посмотреть на журналы нажмите на << 2 >>')
#     print('Чтобы посмотреть на книги нажмите на << 3 >>')
#     print('Чтобы узнать о товарах, нажмите << 5 >>')
#     print('Чтобы посмотреть вашу корзину, нажмите << 6 >>')
#     print('Чтобы выйти нажмите на << 4 >>')

#     try:
#         choice = int(input('Выберите цифру 1/2/3/4/5/6: '))
#     except ValueError:
#         print("Ошибка: пожалуйста, введите корректную цифру.")
#         continue

#     if choice == 4:
#         print('Выход')
#         break

#     elif choice == 1:
#         try:
#             num = int(input('Введите первое число для выбора в меню: '))
#         except ValueError:
#             print("Ошибка: пожалуйста, введите числовые значения.")
#             continue

#         if num == 1:
#             result = 'Это меню выберите что хотите и тд.'
#             print(result)
#         else:
#             print("Ошибка: выберите корректную операцию.")

#     elif choice == 2:
#         result = """1 - Что такое «Секретные войны»: какими будут новые «Мстители» от Marvel
# Как фильм переплюнет «Мстителей: Война бесконечности» и «Мстителей: Финал»
# Капитан Марвел 2 (The Marvels)
# Год выхода: 2023
# Страна: США
# Режиссер: Ниа ДаКоста
# Сценаристы: Ниа ДаКоста, Меган Макдоннел, Элисса Карасик
# Актеры: Бри Ларсон, Тейона Паррис, Иман Веллани, Сэмюэл Л. Джексон, Зави Эштон, Гари Льюис, Пак Со-джун, Зенобия Шрофф, Мохан Капур, Саагар Шайх
# Продолжительность: 1 час 45 минут
# Рейтинг на «Кинопоиске»: 5,2"""
#         print(result)

#     elif choice == 3:
#         result = """Какие 5 книг, которые стоит прочитать?
# Центральная районная библиотека им. М.Ф. Борисова | Список ...
# Итак, список 100 лучших литературных работ, обязательных к прочтению содержит следующие произведения:
# Михаил Булгаков «Мастер и Маргарита»
# Александр Пушкин «Евгений Онегин»
# Федор Достоевский «Преступление и наказание»
# Лев Толстой «Война и мир»
# Антуан де Сент-Экзюпери «Маленький принц»"""
#         print(result)

#     elif choice == 5:
#         print("Наши товары:")
#         print("1. Женская одежда: Платье - 2000 сом")
#         print("2. Мужская одежда: Футболка - 1000 сом")
#         print("3. Аксессуары: Сумка - 1500 сом")
#         print("Чтобы добавить товар в корзину, выберите номер товара.")
#         try:
#             product_choice = int(input("Введите номер товара для добавления в корзину: "))
#             if product_choice == 1:
#                 cart.append('Платье')
#                 print("Платье добавлено в корзину.")
#             elif product_choice == 2:
#                 cart.append('Футболка')
#                 print("Футболка добавлена в корзину.")
#             elif product_choice == 3:
#                 cart.append('Сумка')
#                 print("Сумка добавлена в корзину.")
#             else:
#                 print("Ошибка: выберите корректный товар.")
#         except ValueError:
#             print("Ошибка: пожалуйста, введите корректную цифру.")

#     elif choice == 6:
#         if cart:
#             print("Ваша корзина:")
#             for item in cart:
#                 print(item)
#         else:
#             print("Ваша корзина пуста.")

#     else:
#         print("Ошибка: выберите корректную операцию.")



