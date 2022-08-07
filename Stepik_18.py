# GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение
# суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности. Напишите
# программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) во введенной строке (программа
# не должна зависеть от регистра вводимых символов).

genome = str(input())
new_genome = genome.lower()
cnt = int(new_genome.count('g')) + int(new_genome.count('c'))
print((cnt/len(new_genome))*100)