import sys, os

name_folder = sys.argv[1]
name_file = sys.argv[2]
print(f"Создаю папку {name_folder}")
os.mkdir(name_folder)
print(f'перехожу в папку {name_folder}')
os.chdir(name_folder)

data = "def main():\n\tpass\n\n\nif __name__ == '__main__':\n\tmain()"
print(f"Создаю файл в нашей папке.")
if name_file.split('.')[1] == 'py':
    with open(name_file, 'w') as file:
        file.write(data)
