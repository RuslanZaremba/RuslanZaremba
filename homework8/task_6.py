with open('text_files/task6.txt', encoding='UTF-8') as first1:
    with open('text_files/task6_2.txt', encoding='UTF-8') as second1:
        first = first1.readlines()
        second = second1.readlines()
        for i in range(len(first)):
            if first[i] != second[i]:
                print(i)
