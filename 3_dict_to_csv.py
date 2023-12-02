"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import  csv

user_list =[
    {'name': 'Маша', 'age': 25, 'job': 'Scientist','gender': 'Female'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer','gender': 'Male'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss','gender': 'Male'},
    {'name': 'Nikolay', 'age': 29, 'job': 'Ingineer','gender': 'Male'}
]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
with open('export.csv', 'w') as f:
    fields = ['name', 'age', 'job', 'gender']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)

if __name__ == "__main__":
    main()
