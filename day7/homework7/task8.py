lines = ['asd', 'wqe', 'aasfq']
func = [(lambda i, y: '{}-{}'.format(i, y))(i, lines[i]) for i in range(len(lines))]
print(func)
