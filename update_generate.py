# Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями. Расширения и количество файлов функция принимает в качестве параметров. Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно. Внутри используйте вызов функции из прошлой задачи.

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
        name_length = random.randint(min_name_len, max_name_len)
        file_name = ''.join(random.choices(string.ascii_letters, k=name_length)) + '.' + extension
        file_size = random.randint(min_bytes, max_bytes)
        with open(file_name, 'wb') as f:
            f.write(os.urandom(file_size))
        print(f"Создан файл: {file_name} ({file_size} байт)")

def generate_multiple_extensions(
    extensions_with_counts: dict,
    min_name_len: int = 6,
    max_name_len: int = 30,
    min_bytes: int = 256,
    max_bytes: int = 4096
):
    """
    Генерирует файлы с разными расширениями.

    :param extensions_with_counts: Словарь формата {'txt': 3, 'bin': 5, 'csv': 2}, 
                                   где ключ — расширение, значение — количество файлов.
    :param min_name_len: Минимальная длина имени файла.
    :param max_name_len: Максимальная длина имени файла.
    :param min_bytes: Минимальный размер файла в байтах.
    :param max_bytes: Максимальный размер файла в байтах.
    """
    for extension, count in extensions_with_counts.items():
        print(f"\n🔔 Генерация файлов с расширением: .{extension} (Количество: {count})")
        generate_files(
            extension=extension,
            min_name_len=min_name_len,
            max_name_len=max_name_len,
            min_bytes=min_bytes,
            max_bytes=max_bytes,
            file_count=count
        )


if __name__ == '__main__':
    extensions = {
        'txt': 3,  # 3 текстовых файла
        'bin': 2,  # 2 бинарных файла
        'csv': 4   # 4 CSV-файла
    }

    generate_multiple_extensions(
        extensions_with_counts=extensions,
        min_name_len=8,
        max_name_len=12,
        min_bytes=512,
        max_bytes=1024
    )
