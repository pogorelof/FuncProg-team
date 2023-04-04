file = open('Lab10/text.txt', 'w') #1
file.write('New Line\n2\n3\n4') #2
file.close() #3

file = open('Lab10/text.txt', 'r')
print(file.read()) #4, 5
file.close()

file = open('Lab10/text.txt', 'r')
print("Первая строка: " + file.readline()) #6
print("Вторая строка: " + file.readline(2))
print("Третья строка: " + file.readline(3))
print("Четвертая строка: " + file.readline(4))
print("Файл имеет тип: " + str(type(file))) #7, 8
print("Какие методы доступны для файла: " + str(dir(file))) #9
file.close()

#10
posled = [True, True, False]
print(all(posled))