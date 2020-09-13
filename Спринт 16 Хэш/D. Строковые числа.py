# Евлампии не очень помогло использование легких чисел. 
# Она решила, что будет проще, если превратить все числа в строки. 
# Это касается и дробных чисел. Если при делении двух чисел получается периодическая 
# дробь, нужно вывести период в скобках. Помогите Евлампии определить строковое 
# представление результата деления двух чисел.

# Формат ввода
# В первой строке записано целое неотрицательное число a. 
# Во второй - положительное число b. 
# Оба числа не превосходят 500.

# Формат вывода
# Выведите строковое представление результата вычисления выражения a/b.

# Пример
# Ввод	
# 1
# 2
# Вывод
# 0.5


with open('input.txt') as f:
    n = int(f.readline())
    d = int(f.readline())

def delenie(num, den):

    if not den: 
        return 
    if not num:  
        return "0"
    res = []
    if (num < 0) ^ (den < 0):
        res.append("-") 
    num, den = abs(num), abs(den)
    res.append(str(num//den))
    rmd = num % den
    if not rmd:
        return "".join(res) 
    res.append(".")  
    dic = {}
    while rmd:
        if rmd in dic: 
            res.insert(dic[rmd], "(")
            res.append(")")
            break
        dic[rmd] = len(res) 
        div, rmd = divmod(rmd*10, den)
        res.append(str(div))
    return "".join(res)

print(delenie(n, d))