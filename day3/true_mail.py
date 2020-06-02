ignore_list = '-.'
string = "test@vit-sec.gov.by"
string_list = string.split('@')
for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in '-._':
        print(i)
    else:
        print('Error')
        break
for i in range(0, len(string_list[1]) - 1):
    for v in range(0, len(string_list[1]) - 1):
        if string_list[1][v] in ignore_list and string_list[1][v + 1] in ignore_list:
            print('ji')
        else:
            print('rty')
