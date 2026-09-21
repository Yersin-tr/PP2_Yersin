#1 Функция sorted() может использовать лямбда-выражение в качестве ключа для пользовательской сортировки:
students = [("Эмиль", 25), ("Тобиас", 22), ("Линус", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)