def print_params(a=1, b='строка', c=True):
 
  print(a, b, c)

# Вызовы функции с различным количеством аргументов
print_params()
print_params(10)
print_params(10, "Другая строка")
print_params(10, "Другая строка", False)

# Вызовы с именованными аргументами
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка из списка
values_list = [2, "Список", False]
print_params(*values_list)

# Распаковка из словаря
values_dict = {"a": 3, "b": "Словарь", "c": True}
print_params(**values_dict)

# Распаковка из списка + отдельные параметры
values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)
