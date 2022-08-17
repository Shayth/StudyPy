"""
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили
каким-то странным набором звуков. В какой-то момент один из биологов раскрыл секрет информатиков: они использовали
при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой
символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: Напишите программу, которая умеет шифровать и
расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны
символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно
зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
"""

inp, out, codephrase, decodephrase = [x for x in str(input())], [x for x in str(input())], str(input()), str(input())
dc, codephrase_2, decodephrase_2 = dict(zip(inp, out)), [], []
for x in codephrase:
    codephrase_2 += (str((dc.get(x))).strip(' '))
inv_dc = {v: k for k, v in dc.items()}
for x in decodephrase:
    decodephrase_2.append(str((inv_dc.get(x))).strip())
print(*codephrase_2, sep='')
print(*decodephrase_2, sep='')