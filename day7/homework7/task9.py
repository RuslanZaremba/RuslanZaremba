di = {'a': 2, 'b': 3}
for key, value in di.items():
    print((lambda i, y: {i * 2: y})(key, value))

f = lambda **kwargs: kwargs
print(f(abc='1', abcabc=3, abcabca=4))
