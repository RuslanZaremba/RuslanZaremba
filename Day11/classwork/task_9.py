import sys
import os

name_folder = sys.argv
print(f'Создаем папку с названием {name_folder[1]}')
os.mkdir(name_folder[1])
