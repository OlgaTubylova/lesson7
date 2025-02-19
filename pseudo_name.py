# Напишите функцию, которая генерирует псевдоимена:
# Имя должно начинаться с заглавной буквы,. состоять из 4-7 букв, среди которых. обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random
import string

def pseudo_name(filename):
    vowels = 'aeiou'
    letters_num = random.randint(4, 7)  # длина имени от 4 до 7

    # Случайная позиция для гласной
    vowel_position = random.randint(1, letters_num - 1)

    name = [random.choice(string.ascii_uppercase)]  # первая буква - заглавная

    for i in range(1, letters_num):
        if i == vowel_position:
            name.append(random.choice(vowels))
        else:
            name.append(random.choice(string.ascii_lowercase))

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(''.join(name) + '\n')  

if __name__ == '__main__':
    pseudo_name('names.txt')
