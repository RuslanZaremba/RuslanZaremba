"""Ввести предложение состоящее из двух слов.
Поменять местами слова,
добавить восклицательный знак в начало и конец,
вывести итоговое предложение на экран."""

string = 'hello world'.split()[::-1]
new_string = ' '.join(string)
print(new_string)
print(f"! {new_string} !")
print(f"! {' '.join('Hello world'.split()[::-1])} !")  # ТОЖЕ САМОЕ В ОДНУ СТРОКУ