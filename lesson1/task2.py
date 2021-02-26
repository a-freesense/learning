# Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
# Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".

number = int(input("Введите число:"))
while number != 0:
    sum_numbers = 0
    while number != 0:
        sum_numbers += number % 10
        number = number // 10
    print(sum_numbers)
    number = int(input("Введите число:"))
if number == 0:
    print("Вы ввели 0")