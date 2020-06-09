def sort_string(string):
    """
    Сортирует слова в строке по алфавиту.
    :param string: Строка или слово
    :type: str
    :return: Отсортированную Строку или слово
    :type: str
    """
    new_string = []
    for i in string.split(' '):
        new_string.append(''.join(sorted(i)))
    return ' '.join(new_string)


stro = 'jsdf ewyd lksdvja niaue ldkvj'
print(sort_string(stro))
