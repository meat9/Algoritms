#Выведите двоичное представление этого числа

# Формат ввода
# На вход подается целое число в диапазоне от 0 до 10000.

# Формат вывода
# Выведите двоичное представление этого числа.

# Пример 1
# Ввод	
# 5
# Вывод
# 101
# Пример 2
# Ввод	
# 14
# Вывод
# 1110

n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)