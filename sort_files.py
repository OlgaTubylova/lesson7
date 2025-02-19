# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. Каждая группа включает файлы с несколькими расширениями. В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil
from pathlib import Path

def sort_files_by_extension(source_dir: str, categories: dict):
    """
    Сортирует файлы из указанной папки по категориям в отдельные директории.

    :param source_dir: Путь к исходной папке с файлами.
    :param categories: Словарь формата {'Категория': [расширения]}.
                       Пример: {'Видео': ['.mp4', '.avi'], 'Изображения': ['.jpg', '.png']}
    """
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f" Папка {source_dir} не существует.")
        return

    # Проходим по всем файлам в исходной папке
    for file in source_path.iterdir():
        if file.is_file():
            moved = False  # Флаг, чтобы отследить, был ли файл перемещён
            for category, extensions in categories.items():
                if file.suffix.lower() in extensions:
                    target_dir = source_path / category
                    target_dir.mkdir(exist_ok=True)  # Создаём папку для категории, если её нет
                    shutil.move(str(file), target_dir / file.name)  # Перемещаем файл
                    print(f"{file.name} → {category}")
                    moved = True
                    break
            if not moved:
                print(f"⚠️ Файл {file.name} не подошёл ни под одну категорию и остался на месте.")

if __name__ == '__main__':
    categories = {
        'Видео': ['.mp4', '.avi', '.mkv'],
        'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
        'Текст': ['.txt', '.docx', '.pdf'],
        'Аудио': ['.mp3', '.wav'],
        'Архивы': ['.zip', '.rar', '.7z'],
    }

    # Пример: сортировка файлов в папке 'downloads'
    sort_files_by_extension('downloads', categories)