def nod(a, b):
    """
    Находим НОД чисел a,b.
    :param a: число a
    :type: int
    :param b: число b
    :type: int
    :return: НОД a,b
    :type:int
    """
    count = 1
    nod_a = []
    nod_b = []
    nod_ab = []
    while count <= a or count <= b:
        if a % count == 0:
            nod_a.append(count)
        if b % count == 0:
            nod_b.append(count)
        count += 1
    for i in nod_a:
        if i in nod_b:
            nod_ab.append(i)
    return max(nod_ab)


def nok(a, b):
    return a * b / nod(a, b)


print(nok(9, 12))
