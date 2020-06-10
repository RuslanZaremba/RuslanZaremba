def change_registr(word):
    big = 0
    small = 0
    for i in word:
        if i.isupper():
            big += 1
        else:
            small += 1
    if big > small:
        word = word.upper()
    else:
        word = word.lower()
    return print(word)


change_registr('asdASD')
