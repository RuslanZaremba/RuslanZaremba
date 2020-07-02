import sys

args = sys.argv
total = 0
for i in args:
    if i.isdigit():
        total += int(i)
print(total)


