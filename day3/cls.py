import math

string = 'hello world'.split()[::-1]
print(string)
new_string = ' '.join(string)
print(new_string)
print(f"! {new_string} !")
print(f"! {' '.join('Hello world'.split()[::-1])} !")  # ТОЖЕ САМОЕ В ОДНУ СТРОКУ

string = input()
if len(string) == 0:
    print('Строка пустая')
if len(string) % 3 == 0:
    print(f"{string}!")

string = 'hello world code'.split()
if 'code' in string:
    print('Yes')
else:
    print("no")

age = int(input())
if age < 0:
    print('Wrong input')
elif age < 18:
    print('CocaCola')
else:
    print('Beer')

string=input('Введите строку: ')
if len(string) > 5:
    print(string)
elif len(string) < 5:
    print('Need more!')
else:
    print('It is five')


a = int(input())
b = int(input())
c = int(input())
try:
    d = b ** 2 - 4 * a * c
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)

    if x1 != x2:
        print(f"x1: {x1} x2: {x2}")
    elif x1 == x2:
        print(f"x1, x2 = {x1}")
except:
    print('No')

mail = input('Введите почту: ')
if mail.split('@')[1] == 'gmail.com':
    print(mail)
else:
    print('DOMEN NAME is not supported')
#========================================================================================================
string = '7 TBX 0912'
tax_list = ['TAX', 'TBX', 'TEX']
tax_other = ['TAX', 'TBX']
list_number = string.split()
try:
    if len(tax) == 10:
        if 1 <= int(list_number[0]) <= 7:
            if int(list_number[0]) == 7 and list_number[1] in tax_list:
                if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                    print('Correct')
            elif int(list_number) != 7 and list_number[1] in tax_other:
                if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) >0:
                    print('Correct')
except:
    print('Value error')
#==========================================================================================================
ignore_list = '-.'
string = "test@vit-sec.gov.by"
string_list = string.split('@')
for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in '-._':
        print(i)
    else:
        print('Error')
        break
for i in range(0, len(string_list[1]) - 1 ):
    if j in ignore_list and j + 1 not in ignore_list:
        print('True')