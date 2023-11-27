"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today =datetime.now()
    yesterday = today.replace(day=today.day-1)
    month_ago = today.replace(month=today.month-1)
    print(today.strftime('%d.%m.%Y'))
    print(yesterday.strftime('%d.%m.%Y'))
    print(month_ago.strftime('%d.%m.%Y'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string,'%d/%m/%Y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
