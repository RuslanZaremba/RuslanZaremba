my_list = ['9',
           '7 TAX 9215',
           '6 TEX 9125',
           'a236ye 73',
           '21-14 BOT',
           '3412 0321 GR',
           '1TBX 0021-7',
           '2-TBX 0001',
           '1 TBX 0000',
           '1 TBX 0020']
count = 0
for i in my_list:
    string = i
    tax_list = ['TAX', 'TBX', 'TEX']
    tax_other = ['TAX', 'TBX']
    list_number = string.split()
    try:
        if len(string) == 10:
            if 1 <= int(list_number[0]) <= 7:
                if int(list_number[0]) == 7 and list_number[1] in tax_list:
                    if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                        count += 1
                elif int(list_number[0]) != 7 and list_number[1] in tax_other:
                    if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                        count += 1

    except:
        print("Value error")
print(count)
