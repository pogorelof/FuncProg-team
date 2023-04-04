# Напишите функцию, которая принимает на вход два аргумента - функции
# f и g - и возвращает новую функцию h(x), которая является композицией
# функций f(g(x)). Однако, функции f и g неизвестны заранее и должны
# задаваться пользователем в процессе работы программы

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def square(x):
    return x ** 2

def double(x):
    return 2 * x

new_func = compose(square, double)

result = new_func(5)

print(result)
