with open('text_files/task4.txt') as file:
    file = file.read()

with open('text_files/task4_new.txt', 'w') as new_file:
    changed_0_in_file = file.replace('0', '{nul}').replace('1', '0').replace('{nul}', '1')
    new_file.write(changed_0_in_file)
