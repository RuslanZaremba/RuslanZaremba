a = [1, 59, 120]
for i in range(len(a))[::-1]:
    if a[i] > 59:
        a[i - 1] += a[i] // 60
        a[i] = a[i] % 60
print(a)
