# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: 
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.


import os
import random
import string

def generate_files(
    extension: str,
    min_name_len: int = 6,
    max_name_len: int = 30,
    min_bytes: int = 256,
    max_bytes: int = 4096,
    file_count: int = 42
):
    """Создаёт файлы с указанным расширением, случайными именами и случайным содержимым."""

    for _ in range(file_count):
        # 1Генерируем случайную длину имени файла в заданном диапазоне
        name_length = random.randint(min_name_len, max_name_len)

        # Генерируем случайное имя из букв (строчные + заглавные)
        file_name = ''.join(random.choices(string.ascii_letters, k=name_length)) + '.' + extension

        # Определяем случайный размер файла (в байтах)
        file_size = random.randint(min_bytes, max_bytes)

        # Генерируем случайные байты и записываем их в файл
        with open(file_name, 'wb') as f:
            random_bytes = os.urandom(file_size)  # создаёт байты заданного размера
            f.write(random_bytes)

        print(f"Создан файл: {file_name} ({file_size} байт)")

if __name__ == '__main__':
    # Пример: создадим 5 файлов с расширением 'bin', именами длиной 8-12, размером 512-1024 байт
    generate_files('bin', min_name_len=8, max_name_len=12, min_bytes=512, max_bytes=1024, file_count=5)
