#1 Функция map() применяет функцию к каждому элементу итерируемого объекта:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#2 
numbers = [1, 2, 3, 4, 5]
# Lambda применяется к каждому элементу списка 
# Каждый элемент умножается на 2 
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#3 