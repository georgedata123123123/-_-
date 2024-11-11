# Выполнил: Георгий Павлович Мальцев



a = [3, 7, 9, 16, 19, 25, 38, 39, 43]
print(a)
# искомое число
value = int(input())

# индексы первого элемента, последнего и среднего
low = 0
high = len(a) - 1
mid = len(a) // 2

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print('No value')
else:
    print('ID =', mid)

