'''
Реализуйте программу, которая будет вычислять количество различных объектов в списке. Два объекта a и b считаются
различными, если a is b равно False. Вашей программе доступна переменная с названием objects, которая ссылается на
список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.
'''


second_list = []
for obj in objects:  # доступная переменная objects
    if obj not in second_list:
        second_list.append(obj)
ans = len(second_list)
print(ans)