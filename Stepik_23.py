# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел
# не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел. Гарантируется, что в какой-то
# момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно. В примере мы считываем
# числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов,
# не обращая внимания на то, что остались ещё не прочитанные значения.

list1, list_square = [],[]
list1.append(int(input()))
while sum(list1) != 0:
    list1.append(int(input()))
list_square.extend(i ** 2 for i in list1)
print(sum(list_square))