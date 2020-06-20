with open('text_files/task1.txt', 'r', encoding='utf-8') as file:
    arr = file.readlines()
    count_lines = len(arr)
    count_items = []
    count_words = []
    for line in arr:
        count_items.append(f"{str(len(line.rstrip().replace(' ', '')))}")
    for word in arr:
        count_words.append(f"{len(list((filter(lambda x: x.isalpha(), word.rstrip().split(' ')))))}")
    print(count_words)

with open('text_files/text_for_task10.txt', 'w', encoding='utf-8') as file:
    for i in range(len(count_items)):
        file.write(f"Количество знаков в строке: {count_items[i]}, колличество слов {count_words[i]} \n")
    file.write(f"Всего строк: {count_lines}")
