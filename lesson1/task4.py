# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

number = 1
while number <= 100:
    if number % 10 == 0 or number % 10 == 5 or number % 10 == 6 or number % 10 == 7 or number % 10 == 8 or number % 10 == 9 or number % 100 == 14 or number % 100 == 11 or number%100 == 12 or number%100 == 13:
        print(f"{number} процентов")
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        print(f"{number} процента")
    elif number % 10 == 1:
        print(f"{number} процента")
    number += 1


