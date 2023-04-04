user_str = input('Введите строку: ')
set_of_letters = set()

for letter in user_str:
    set_of_letters.add(letter)

list_of_letters = list(set_of_letters)
list_of_letters.sort()
print(*list_of_letters)