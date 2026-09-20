#создание функции
def my_function():
  print("Hello from a function")
#вызов функции
def my_function():
  print("Привет из функции")

my_function()
#одну и ту же функцию можно вызвать столько раз, сколько угодно 
def my_function():
  print("Привет из функции")

my_function()
my_function()
my_function()
# С использованием функций — многократно используемый код:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))