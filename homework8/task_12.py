with open('text_files/text_12.txt') as file:
    for num in file.read().rsplit():
        print(sum(int(c) for c in str(num)), end=' ')