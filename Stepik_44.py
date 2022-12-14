"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов. Напишите программу,
которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося. Файл состоит из набора строк,
каждая из которых представляет собой три поля: Класс Фамилия Рост Класс обозначается только числом. Буквенные
модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве
роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного
числа. Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по
одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк. В качестве ответа
прикрепите файл с полученными данными о среднем росте.
"""
class_rawinfo = {}
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
with open('dataset.txt') as inp:
    for line in inp:
        string = line.rstrip().split('\t')
        if string[0] not in class_rawinfo:
            class_rawinfo[string[0]] = [int(string[2]), 1]
        elif string[0] in class_rawinfo:
            heights = class_rawinfo[string[0]][0] + int(string[2])
            students = class_rawinfo[string[0]][1] + 1
            class_rawinfo[string[0]] = [heights, students]
for k, v in class_rawinfo.items():
    class_info[int(k) - 1] = v[0] / v[1]
with open('output.txt', 'w') as outp:
    for i in range(len(class_info)):
        output = str(i + 1) + ' ' + str(class_info[i]) + '\n'
        outp.write(output)