"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов. Если введённое
слово не найдено в этом списке, оно помечается как "ошибка". Попробуем написать подобную систему. На вход
программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти
слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста. Выведите уникальные
"ошибки" в произвольном порядке. Работу производите без учёта регистра.
"""

amount_known_words, known_words_lst = int(input()), []
for i in range(amount_known_words):
    x = input().lower()
    if x not in known_words_lst:
        known_words_lst.append(x)
amount_check_phrase, check_words = int(input()), []
for j in range(amount_check_phrase):
    x = input().lower().split()
    for i in x:
        if i not in known_words_lst and i not in check_words:
            check_words.append(i)
print('\n'.join(check_words))