# Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst. Позиции нумеруются с нуля,
# если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы). Позиции должны
# быть выведены в одну строку, по возрастанию абсолютного значения.

list1, x = [int(i) for i in input().split()], int(input())
index = [i for i, a in enumerate(list1) if a == x]
print('Отсутствует') if index == [] else print(*index)

