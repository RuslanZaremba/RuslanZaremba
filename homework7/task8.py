lines = ['asd', 'wqe', 'aasfq']
for i in range(len(lines)):
    s = list(map(lambda i: '{} - {}'.format(i, lines[i]), lines))
    print(s)
