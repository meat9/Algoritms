
# Нужно реализовать класс StackMax, который поддерживает операцию определения максимума 
# среди всех элементов в стеке. Класс также должен поддерживать все операции, реализованные 
# в классе Stack, из урока. При этом в классе StackMax может быть реализовано не более трёх 
# методов.
# Стек может содержать только данные типов, поддерживающих операцию сравнения. 
# Иначе операция поиска максимума будет некорректной.
# Формат ввода
# В первой строке записано одно число n - количество команд. n не превосходит 1000. 
# В следующих n строках идут команды. Команды могут быть следующих видов:
# push x - добавить число x в стек
# pop - удалить число с вершины стека
# get_max - напечатать максимальное число в стеке
# Если стек пуст при вызове команды get_max нужно напечатать None, для команды pop - error.
# Формат вывода
# Для каждой команды get_max напечатайте результат её выполнения. 
# Если стек пустой, для команды get_max напечатайте None. 
# Если происходит удаление из пустого стека - напечатайте error.
# Пример 1
# Ввод	
# 8
# get_max
# push 7
# pop
# push -2
# push -1
# pop
# get_max
# get_max
# Вывод
# None
# -2
# -2
# Пример 2
# Ввод	
# 7
# get_max
# pop
# pop
# pop
# push 10
# get_max
# push -9
# Вывод
# None
# error
# error
# error
# 10

class StackMax:
    items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            print('error')
            return
        return self.items.pop()
    def get_max(self):
        if len(self.items) == 0:
            print('None')
            return
        print(max(self.items))
        return
t = int(input())
stack = StackMax()
while t:
    l = input().split()
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        stack.pop()
    if l[0] == 'get_max':
        stack.get_max()
    t -= 1