ignore_list = '-.'
string = "test@vit-sec.gov-.by"
string_list = string.split('@')
for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in '-._':
        print(i)
    else:
        print('Error')
        break
for i in range(len(string_list[1]) - 1):
    for j in range(len(string_list[1]) - 1):
        if string_list[1][j] in ignore_list and string_list[1][j+1] in ignore_list:
            print('Ошибка адреса')
