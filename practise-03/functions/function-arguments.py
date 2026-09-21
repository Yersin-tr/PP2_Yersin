#1  Функции с 1 аргументам
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# 2 
def my_function(name): # name — это параметр
  print("Hello", name)

my_function("Emil") # "Emil" — это аргумент
#3 Эта функция ожидает 2 аргумента и получает 2 аргумента::
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#4 Значения параметров по умолчанию
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")