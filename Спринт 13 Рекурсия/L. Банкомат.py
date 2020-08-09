# Тимофей пошел снять деньги в банкомат. Ему нужно n трешландийских долларов. 
# В банкомате в бесконечном количестве имеется n монет различных достоинств. 
# Нужно определить число способов, которыми Тимофей сможет набрать нужную сумму.

# Формат ввода
# В первой строке записано m - сумма, которую нужно набрать. 
# Во второй стоке n - количество монет в банкомате. Оба числа не превосходят 300. 
# Далее в строку записано n чисел, каждое в диапазоне от 1 до 1000.

# Формат вывода
# Нужно вывести число способов, которым Тимофей сможет набрать нужную сумму.

# Пример 1
# Ввод	
# 5
# 3
# 1 2 3
# Вывод
# 5

def count(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
  
    return table[n] 
with open("input.txt") as f:
    n = int(f.readline())
    m = int(f.readline())
	
    arr = list(map(int, (f.readline().split())))

print (count(arr, m, n)) 