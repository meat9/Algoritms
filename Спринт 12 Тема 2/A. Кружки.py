# Напишите код для решения задачи про поиск кружков, которые посещает хотя бы один ученик. 
# Ваше решение должно задействовать O(1) дополнительной памяти (то есть помимо памяти, 
# выделенной под массив visited_optional_courses)

# Формат ввода
# В первой строке записано количество кружков n, целое число, не превосходящее 10000 
# В следующих n строках записаны названия кружков.

# Формат вывода
# Выведите уникальные названия кружков по одному на строке, в порядке появления во 
# входных данных.

# Пример
# Ввод	
# 8
# вышивание крестиком
# рисование мелками на парте
# настольный керлинг
# настольный керлинг
# кухня африканского племени ужасмай
# тяжелая атлетика
# таракановедение
# таракановедение
# Вывод
# вышивание крестиком
# рисование мелками на парте
# настольный керлинг
# кухня африканского племени ужасмай
# тяжелая атлетика
# таракановедение
x = int(input())
m = []
for i in range(x):
    m.append(input())
visited_optional_courses = list()
for course in m:
    if course not in visited_optional_courses:
        visited_optional_courses.append(course)

print ("\n".join(visited_optional_courses))