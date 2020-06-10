def funct_16(a):
    dict_16 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
               15: 'F'}
    num_in_16 = []
    i = a
    while i != 0:
        num_in_16.insert(0, dict_16.get(i % 16))
        i = i // 16
    return print(''.join(map(str, num_in_16)))


funct_16(331)
