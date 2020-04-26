# Занятие_#4.
# задача_4.1 Функция (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
print('Задача_#4.1')
text_1 = """Функция (F): на вход список имен и целое число N;
на выходе список длины N случайных имен из первого списка (могут повторяться,
можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);"""
print(text_1)
print()

import random
def func_list_random(name_list, n):
    length_name_list = len(name_list)
    new_name_list = []
    for i in range(n):
        j = random.randint(0, len(name_list) - 1)
        new_name_list.append(name_list[j])
    return new_name_list

name_list_1 = ('Roman', 'Sveta', 'Nikita', 'Fufik', 'Kod', 'Danila', 'Vasja', 'Kirill', 'Nina', 'Kuzja', 'Toshka', 'Valentin', 'Gena', 'Karat', 'Mihail', 'Vlad', 'Klava', 'Jula', 'Vova', 'Vanja')
name_list_2 = func_list_random(name_list_1, 100)
print(name_list_2)
print('длина нового списка равна: ', len(name_list_2))

print('*'*100)
print('*'*100)

# задача_4.2: Написать функцию вывода самого частого имени из списка на выходе функции F из задачи__#4.1;
print('Задача_#4.2')
text_2 = 'функция вывода самого частого имени из списка на выходе функции F из задачи__#4.1'
print(text_2)
print()

def max_frequency(name_list):
    dict = {}
    count, word = 0, ''
    for el in reversed(name_list):
        dict[el] = dict.get(el,0) + 1
        if dict[el] >=count :
            count, word = dict[el], el
    return (word, count)
print(max_frequency(name_list_2))

print('*'*100)
print('*'*100)

# задача_4.3: Написать функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
print('Задача_#4.3')
text_3 = 'Написать функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.'
def min_letter_frequency(name_list):
    letter_list = []
    for i in range(len(name_list)):
        letter = str(name_list[i])
        letter = letter[0]
        letter_list.append(letter)
    dict = {}
    count_letr = len(name_list)
    letter = ''
    for el in letter_list:
        dict[el] = dict.get(el,0) + 1
        if dict[el] <= count_letr :
            count_letr, letter = dict[el], el
    return (letter, count_letr)
print(min_letter_frequency(name_list_2))