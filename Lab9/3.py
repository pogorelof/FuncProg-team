# Приведите свой пример с использованием функций Map, Filter и
# Reduce. Выясните отличия

list_of_points = [50, 70, 80, 45, 39, 70, 20, 52, 61]

#Map
#перевод оценок в 10 бальную систему

def dble(a):
    return a / 10

new_points = map(dble, list_of_points)
print(list(new_points))

#Filter
#возвращает оценки только выше 50

def more50(points):
    return points > 50

new_points = list(filter(more50, list_of_points))
print(new_points) 

#Reduce
#соединяет все именя из списка
from functools import reduce

list_of_students = ['Vladimir', 'Malika', 'Daniyar', 'Ernar']

def concat(student1, student2):
    return student1 + ' ' + student2

new_list = reduce(concat, list_of_students)
print(new_list)