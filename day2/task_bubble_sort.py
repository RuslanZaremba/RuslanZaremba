# Пузырьковая сортировка

arr = [2, 1, 4, 2, 3, 1, 5, 8, 54, 5423, 3, 4, 6, -2]

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
