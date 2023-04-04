# Напишите функциянальную и не функциональную функция, и
# разберите отличие между ними. В качестве параметра можете
# использовать свое резюме.

list_of_students = ['Vladimir', 'Malika', 'Daniyar', 'Ernar']

#функциональная функция
#возвращает какое-либо значение
def FuncFoo(students): #находит общее количество букв во всех ячейках листа
    sum = 0
    for i in students:
        for j in i:
            sum += 1
    return sum

print(FuncFoo(list_of_students))


#нефункциональная функция.
#не возвращает никакие значения
def NotFuncFoo(students):
    for i in list_of_students:
        print(i)

NotFuncFoo(list_of_students)