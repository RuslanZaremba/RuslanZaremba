# ИТЕРАТОРЫ
import re

# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(3)
# for i in s_iter1:
#     print(i)

# ГЕНЕРАТОРЫ

# def simple_generator(val):
#     while val > 0:
#         val -= 1
#         yield 1
#
#
# get_iter = simple_generator(5)
# print(next(get_iter))
# print(next(get_iter))
# print(next(get_iter))
# print(next(get_iter))
# print(next(get_iter))
# print(next(get_iter))

# MODULE RE

# result = re.match(r'AV', 'AV Analys AV')
# print (result.group(0))
# result = re.search(r'Analys', 'AV Analys Vidhya AV')
# print(result.group(0))
# result = re.findall(r'AV', 'AV Analys Vidhya AV')
# print(result)
# result = re.sub(r'India', 'the World', 'Av is largest Analytics community of India')
# print(result)
pattern = re.compile('AV')
res1 = pattern.findall('AV Analytics Vita AV')
print(res1)
res2 = pattern.findall('AV is largest Analytics community of India')
print(res2)