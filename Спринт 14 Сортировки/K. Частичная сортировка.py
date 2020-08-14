# После того, как Гоша узнал про сортировку слиянием и быструю сортировку, 
# он решил придумать свой метод сортировки, который предполагал бы разделение данных на части.
# Назвал он свою сортировку Частичной. 
# Этим методом можно отсортировать n уникальных чисел, 
# находящихся в диапазоне от 0 до n - 1. 
# В соответствии с методом нужно разбить данные на максимально 
# возможное количество частей таким образом, чтобы можно было отсортировать 
# каждую из частей отдельно, соединить, и при этом результат будет отсортирован.
# После сортировки отдельных частей менять части местами нельзя.

# Формат ввода
# В первой строке задано n - количество чисел для сортировки. 
# В следующей строке записан числа от 0 до n - 1, которые нужно 
# отсортировать описанным методом.

# Формат вывода
# Выведите максимальное количество частей, на которое можно разбить данные 
# при использовании метода Частичной сортировки.

# Пример 1
# Ввод	
# 4
# 0 1 3 2
# Вывод
# 3
# Пример 2
# Ввод	
# 8
# 3 6 7 4 1 5 0 2
# Вывод
# 1
# Пример 3
# Ввод	
# 5
# 1 0 2 3 4
# Вывод
# 4