with open('text_files/task1.txt', encoding='UTF-8') as my_file:
    file = my_file.readlines()
    print(f"{file[0]}")
    print(f"{file[4]}")
    print(f"{''.join(file[:5])}")
    print(f"{''.join(file[:2])}")
    my_file.seek(0)
    print(my_file.read())
