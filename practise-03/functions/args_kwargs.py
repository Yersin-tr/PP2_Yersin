#Использование *args для приема любого количества аргументов:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#Параметр *args позволяет функции принимать любое количество позиционных аргументов.
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
#Обычные параметры должны стоять перед *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
#*args полезен, когда нужно создать гибкую функцию:
def my_function(*numbers):
total = 0
  for num in numbers:
total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))