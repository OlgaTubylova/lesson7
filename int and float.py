# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

import random

def fill_file(n, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(n):
            int_num = random.randint(-1000, 1000)
            float_num = round(random.uniform(-1000, 1000), 5)  
            f.write(f'{int_num}|{float_num}\n')


if __name__ == '__main__':
    fill_file(10, 'file.txt')
        