# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
#
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
#
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

interval = int(input("Введите интервал:"))
min = interval // 60
hours = min // 60
days = hours // 24
sec = interval % 60
min = min % 60
hours = hours % 24
if interval < 60:
    print(f"{sec} сек")
elif interval >= 60 and interval < 60 * 60:
    print(f"{min} мин {sec} сек")
elif interval >= 60 * 60 and interval < 60 * 60 * 24:
    print(f"{hours} час {min} мин {sec} сек")
else:
    print(f"{days} дн {hours} час {min} мин {sec} сек")


