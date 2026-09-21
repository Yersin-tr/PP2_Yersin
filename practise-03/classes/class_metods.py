# Создаем класс
class Person:
    def __init__(self, name):
    self.name = name

    # Создаем метод
    def say_hello(self):
        print("Hello, my name is " + self.name)


# Создаем объект
person = Person("Yersin")

# Вызываем метод
person.say_hello()
```
