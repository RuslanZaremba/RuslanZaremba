# from functools import reduce
#
#
# all_max = reduce(lambda a, b: a if (a > b) else b, items)
# print(all_max)

items = [1, 24, 17, 14, 9, 32, 2]
result = max(items, key=lambda x: int(x))
print(result)
# РАЗОБРАТЬ ФУНКЦИЮ max