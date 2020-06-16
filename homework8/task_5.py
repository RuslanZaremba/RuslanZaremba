with open('task2.txt', encoding='UTF-8') as file:
    with open('task5_odd.txt', 'w', encoding='UTF-8') as odd:
        with open('task5_even.txt', 'w', encoding='UTF-8') as even:
            lines = file.readlines()
            for i in range(len(lines)):
                if i % 2 != 0:
                    even.write(lines[i])
                else:
                    odd.write(lines[i])
