#1
# Функция, которая возвращает значение
def get_greeting():
    return "Hello from a function"
message = get_greeting() 
print(message)
# Использование возвращаемого значения напрямую
def get_greeting(): 
    return "Hello from a function"
print(get_greeting())
# Функция, которая возвращает результат вычисления
def fahrenheit_to_celsius(fahrenheit): 
    return (fahrenheit - 32) * 5 / 9
# Функция, которая возвращает результат вычисления
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95)) 
print(fahrenheit_to_celsius(50))