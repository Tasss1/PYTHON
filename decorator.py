def my_decarator(func):
    def wrapper():
        print('Что-то происходит перед вызовом фукнции: ')
        func()
        print('Что-то происходит после вызовом фукнции:')
    return wrapper()

@my_decarator
def say_hello():
    print('Привет!')
