# Напишите функцию в результате которая возвращает список, кортеж
# и слоаварь. Пример должен быть индивидуальным


def Foo():
    list = []
    dict = {}
    for i in range(3):
        name = input('Введите имя: \n')
        age = input('Введите возраст: \n')
        list.append(name)
        dict[name] = age
    tuple = ('Количество человек в списке', len(list))
    return list, tuple, dict

list, tuple, dict = Foo()

print(list)
print(dict)
print(tuple)
