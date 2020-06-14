lines = ['asd', 'wqe', 'aasfq']
a = [(lambda i: '{}-{}'.format(i, a[i]))(i) for i in range(len(a))]
print(a)
