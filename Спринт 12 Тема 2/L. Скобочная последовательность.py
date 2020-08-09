# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов. 
# Если вы с ней еще не сталкивались, то наверняка столкнётесь — она довольно популярная.
# Дана скобочная последовательность. Нужно определить, правильная ли она.
# Будем придерживаться такого определения:
# - пустая строка — правильная скобочная последовательность;
# - правильная скобочная последовательность, взятая в скобки одного типа, — 
# правильная скобочная последовательность;
# - правильная скобочная последовательность с приписанной слева или справа правильной 
# скобочной последовательностью — тоже правильная.
# На вход подается последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную 
# последовательность и возвращает True, если последовательность правильная, иначе False.

# Формат ввода
# На вход подается одна строка, содержащая скобочную последовательность.

# Формат вывода
# True или False.

# Пример 1
# Ввод	
# {[()]}
# Вывод
# True
# Пример 2
# Ввод	
# ()
# Вывод
# True

def is_correct_bracket_seq(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return not text
print(is_correct_bracket_seq(input()))