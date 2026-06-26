import random

# 1) Создать целочисленный массив из 10 элементов
array = [random.randint(1, 100) for _ in range(10)]

# 2) Функция вывода массива
def print_array(arr):
    for i in range(len(arr)):
        print(f"arr[{i}] = {arr[i]}")

# 3) Функция поиска максимального элемента
def find_max(arr):
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i

    return max_index

# Вывод массива
print("Массив:")
print_array(array)

# Поиск максимального элемента
max_index = find_max(array)
print(f"\nМаксимальный элемент: arr[{max_index}] = {array[max_index]}")