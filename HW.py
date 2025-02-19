# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path

def batch_rename_files(
    directory: str,
    desired_name: str,
    digits: int,
    source_extension: str,
    target_extension: str,
    name_range: tuple[int, int]
):
    """
    Переименовывает файлы в указанной папке согласно заданным параметрам.

    :param directory: Папка с файлами для переименования.
    :param desired_name: Желаемое конечное имя файлов. В конце добавляется порядковый номер.
    :param digits: Количество цифр в порядковом номере.
    :param source_extension: Расширение исходных файлов (например, 'txt' или '.txt').
    :param target_extension: Расширение конечных файлов (например, 'md' или '.md').
    :param name_range: Кортеж (start, end), указывающий диапазон сохраняемой части оригинального имени.
    """
    source_path = Path(directory)
    if not source_path.exists():
        print(f"Папка {directory} не существует.")
        return

    # Приведение расширений к единому формату (добавление точки, если отсутствует)
    source_extension = f".{source_extension.lstrip('.')}"
    target_extension = f".{target_extension.lstrip('.')}"

    files_to_rename = [file for file in source_path.iterdir() if file.is_file() and file.suffix == source_extension]
    files_to_rename.sort()  # Для стабильного порядка переименования

    if not files_to_rename:
        print(f"Нет файлов с расширением {source_extension} для переименования.")
        return

    for counter, file in enumerate(files_to_rename, start=1):
        original_name = file.stem  # Имя файла без расширения
        start, end = name_range

        # Коррекция диапазона, если он выходит за границы
        start = max(1, start)
        end = min(len(original_name), end)

        preserved_part = original_name[start - 1:end] if start <= end else ''

        # Формируем порядковый номер с ведущими нулями
        number = str(counter).zfill(digits)

        # Формируем новое имя файла
        new_name = f"{preserved_part}{desired_name}{number}{target_extension}"

        try:
            file.rename(source_path / new_name)
            print(f"{file.name} → {new_name}")
        except Exception as e:
            print(f"Ошибка при переименовании {file.name}: {e}")


if __name__ == '__main__':
    folder_name = '/Users/olgatubylova/Documents/CS/Python/DataEngineer/Seminar/lesson_7'
    
    # Запускаем переименование
    batch_rename_files(
        directory=folder_name,
        desired_name="new_name",
        digits=3,
        source_extension="txt",
        target_extension="md",
        name_range=(3, 6)
    )