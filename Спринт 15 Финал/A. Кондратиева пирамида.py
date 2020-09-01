# В Трешландии проводились ежегодные соревнования по заезду на барсучьих упряжках. 
# Нужно обработать результаты забегов. Данные представлены в формате: 
# имя участника - список заработанных очков
# Нужно отсортировать данные по такому принципу:
# Если сумма набранных очков участника A больше, чем у участника В, то А 
# должен идти в списке раньше. При подсчете суммы нужно учитывать только 
# положительные значения очков.
# Если суммы равны, то первым должен идти участник, чье имя лексикографически меньше.
# При совпадении имен раньше должен идти участник, который во входных данных находится позже. 
# При этом, если из имени участника можно составить английский вариант имени Кондратий 
# (например, если имя nekondratiy или drkonxxxiyatt), то все правила отменяются. 
# Он должен идти в списке раньше. Если таких участников больше одного, 
# то раньше должен идти тот, кто находится позже во входных данных. 
# (Заработанные очки не рассматриваются).

# Формат ввода
# В первой строке задано n - число участников. Оно не превосходит 10000. 
# В следующих n строках записана информация о каждом из участников в обозначенном формате. 
# Имя состоит из строчных латинских букв. Длина имени не превосходит 100.
# Длина списка набранных очков не больше 1000. Каждое из очков по модулю не превосходит 1000.

# Формат вывода
# Нужно вывести данные в отсортированном порядке в таком же формате.

# Пример 1
# Ввод	
# 3
# anna 1 -4 5 0 1
# sam 1 9 5 0 1
# kondratiy 1 9 5 0 -1
# Вывод
# kondratiy 1 9 5 0 -1
# sam 1 9 5 0 1
# anna 1 -4 5 0 1

class Barsukmeeting:
    def __init__(self, data, pos):
        self.data = data
        data = data.split(' ')
        self.score = sum([int(i) for i in data[1:] if int(i) > 0])
        self.name = data[0]
        self.rule = set('kondratiy').issubset(self.name)
        self.pos = pos
    
    def __gt__(self, other):
        if self.rule and other.rule:
            return self.pos > other.pos
        elif not self.rule and not other.rule:
            if self.score == other.score:
                if self.name == other.name:
                    return self.pos > other.pos
                return self.name < other.name
            return self.score > other.score
        elif self.rule and not other.rule:
            return True
        elif not self.rule and other.rule:
            return False
    
    def __repr__(self):
        return self.data


def heapify(array, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[i] > array[left]:
        root = left
    if right < n and array[root] > array[right]:
        root = right
    if root != i:
        array[i], array[root] = array[root], array[i]
        heapify(array, n, root)


def heapsort(array, n):
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == "__main__":
    heap = []
    with open('input.txt') as f:
        n = int(f.readline())
        for pos in range(n):
            heap.append(Barsukmeeting(f.readline().strip(), pos))
    heapsort(heap, n)
    for elem in heap:
        print(elem)
