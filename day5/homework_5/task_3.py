def degree(a, n):

    result = a
    counnter = n
    while counnter != 1:
        result = result * a
        counnter -= 1
    return result


x = int(input('Введите число: '))
y = (degree(x, 6) * degree((x - 5), 3)) / degree((2 * x + 1), 5)
print(y)
