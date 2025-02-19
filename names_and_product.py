# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало.

# with (
#     open('file.txt', 'r', encoding='utf-8') as f1,
#     open('names.txt', 'r') as f2,
#     open('new_names and product.txt', 'a') as f3

# ):
    
from itertools import cycle

def process_files(numbers_file, names_file, output_file):
    with (
        open(numbers_file, 'r', encoding='utf-8') as f1,
        open(names_file, 'r', encoding='utf-8') as f2,
        open(output_file, 'w', encoding='utf-8') as f3  
    ):
        numbers_lines = f1.readlines()
        names_lines = f2.readlines()

        # Определяем более длинный список для количества строк в выходном файле
        max_len = max(len(numbers_lines), len(names_lines))

        # Итераторы: длинный список проходим напрямую, короткий — с cycle (бесконечный повтор)
        numbers_iter = cycle(numbers_lines) if len(numbers_lines) < max_len else iter(numbers_lines)
        names_iter = cycle(names_lines) if len(names_lines) < max_len else iter(names_lines)

        for _ in range(max_len):
            numbers_line = next(numbers_iter).strip()  # пример: "-665|685.94881"
            name_line = next(names_iter).strip()       # пример: "CfyQIfAmnde"

            # Разделяем числа по разделителю '|', преобразуем к float
            num1_str, num2_str = numbers_line.split('|')
            num1, num2 = float(num1_str), float(num2_str)

            product = num1 * num2  

            if product < 0:
                f3.write(f"{name_line.lower()} | {abs(product)}\n")
            else:
                f3.write(f"{name_line.upper()} | {round(product)}\n")


if __name__ == '__main__':
    process_files('file.txt', 'names.txt', 'new_names_and_product.txt')

