def binary_search(arr: list, target: int):
    # Начальные значения границ
    left, right = 0, len(arr) - 1

    while left <= right:
        # Середина массива
        mid = (left + right) // 2

        # Если средний элемент — это искомый
        if arr[mid] == target:
            return mid  # Возвращаем индекс

        # Если средний элемент больше искомого, сужаем поиск до левой части
        elif arr[mid] > target:
            right = mid - 1

        # Если средний элемент меньше искомого, сужаем поиск до правой части
        else:
            left = mid + 1

    # Если элемент не найден
    return -1


# Пример использования:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Элемент найден на индексе {result}")
else:
    print("Элемент не найден")
