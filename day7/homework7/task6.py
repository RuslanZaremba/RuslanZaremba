from functools import reduce

nums = [10, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]

new_list = reduce(lambda a, b: a * b, filter(lambda x: not x % 3, nums))
print(new_list)

# КАК НУЖНО СДЕЛАТЬ?
result = reduce(lambda x, y: x * y if y % 3 == 0 else x, nums)
print(result)
