# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы
# информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке. Кодирование
# осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов
# исходной строки заменяются на этот символ и количество его повторений в этой позиции строки. Напишите программу,
# которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на
# стандартный вывод. Кодирование должно учитывать регистр символов.

uncoded = str(input())
l = len(uncoded) - 1
c = 1
t = ''
if len(uncoded) == 1:
    t = t + uncoded + str(c)
else:
    for i in range(0, l):
        if uncoded[i] == uncoded[i + 1]:
            c += 1
        elif uncoded[i] != uncoded[i + 1]:
            t = t + uncoded[i] + str(c)
            c = 1
    for j in range(l, l + 1):
        if uncoded[-1] == uncoded[-2]:
            t = t + uncoded[j] + str(c)
        elif uncoded[-1] != uncoded[-2]:
            t = t + uncoded[j] + str(c)
            c = 1
print(t)
