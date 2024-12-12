# def num(x,y):
#     return x + y
# print(num(5,10))

# def main():
#     print('hello')
#     print('world')
#     print('Salam')

# main()
# print('goodbye')
# main()
    

# def calcu():
#     num1 = float(input('Введите первое число: '))
#     operator = input('Введите оператор (+, -, *, /): ')
#     num2 = float(input('Введите второе число: '))

#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         print('Неверный оператор!')
#         return

#     print('Результат:', result)

# calcu()


# import random

# def choice ():
#     choice = random.randint(1,2)

#     if choice == 1:
#         print('Орел')

#     elif choice == 2:
#         print('решка')

# choice()

# import random
#
# def shislo():
#     get = random.randint(1, 100)
#     print("Добро пожаловать в игру 'Угадай число'!")
#     print("Я загадал число от 1 до 100. Попробуй угадать его!")
#


# import random

# def shislo():
#     get = random.randint(1, 100)
#     print("Добро пожаловать в игру 'Угадай число'!")
#     print("Я загадал число от 1 до 100. Попробуй угадать его!")

#     while True:
#             geer = int(input("Введите ваше предположение: "))
            
#             if geer < get:
#                 print("Загаданное число больше.")
#             elif geer > get:
#                 print("Загаданное число меньше.")
#             else:
#                 print("Поздравляю! Вы угадали число!")
#                 break
# shislo()


# number = int(input('Выберите число: '))
# def shislo(n):
#     if n % 2 == 0:
#         print(f'{n}сложный')
#     elif n % 1 == 0:
#         print(f'{n}обычный')

# shislo(number)





# Тапшырма: 1)Функция текстти кабыл алып, аны тескери кылып кайтарып берсин.

# 2)Функция тизмедеги эң чоң жана эң кичине сандарды кайтарып берсин.

# 3)Функция жазып, берилген санды берилген даражага көтөрсүн.

# 4) Функция берилген тексттеги бардык сөздөрдүн баш тамгасын чоң кылып кайтарып берсин.

# 5) Берилген сан оңбу, терсби же нөл экенин текст катары кайтарып берген функция жазыңыз.



def тескери(текст):
    return текст[::-1]

# Тест
print(тескери("Салам"))  # Жыйынтык: "малас"
print(тескери("Python"))  # Жыйынтык: "nohtyP"

def чоң_кичине(тизме):
    чоң = max(тизме)
    кичине = min(тизме)
    return чоң, кичине

# Тест
print(чоң_кичине([3, 7, 1, 9]))  # Жыйынтык: (9, 1)
print(чоң_кичине([10, 20, 5, 8]))  # Жыйынтык: (20, 5)

def даража(сан, даража):
    return сан ** даража

# Тест
print(даража(2, 3))  # Жыйынтык: 8
print(даража(5, 2))  # Жыйынтык: 25


def баш_тамга(текст):
    return текст.title()

# Тест
print(баш_тамга("салам дүйнө"))  # Жыйынтык: "Салам Дүйнө"
print(баш_тамга("python программалоо"))  # Жыйынтык: "Python Программалоо"

def сан_текшерүү(сан):
    if сан > 0:
        return "Оң сан"
    elif сан < 0:
        return "Терс сан"
    else:
        return "Нөл"

# Тест
print(сан_текшерүү(5))   # Жыйынтык: "Оң сан"
print(сан_текшерүү(-3))  # Жыйынтык: "Терс сан"
print(сан_текшерүү(0))   # Жыйынтык: "Нөл"