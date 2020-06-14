from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]

new_list = reduce(lambda a, b: a * b, list(filter(lambda x: not x % 3, nums)))
print(new_list)
