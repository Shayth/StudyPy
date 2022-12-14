"""
Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида: север 10 запад 20 юг
30 восток 40, где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это
положительное расстояние в сантиметрах, которое должна пройти черепашка.
Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу,
которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу,
которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать,
что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего n строк с самими
командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все
координаты целочисленные.
"""

x, y = 0, 0
n = int(input())
for a in range(n):
    command = str(input())
    if command.startswith('север'):
        for i in command.split():
            if i.isdigit():
                x = x + int(i)
    if command.startswith('восток'):
        for i in command.split():
            if i.isdigit():
                y = y + int(i)
    if command.startswith('юг'):
        for i in command.split():
            if i.isdigit():
                x = x - int(i)
    if command.startswith('запад'):
        for i in command.split():
            if i.isdigit():
                y = y - int(i)
print(y, x)