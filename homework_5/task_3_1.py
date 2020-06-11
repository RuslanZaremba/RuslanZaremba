pupils = [
    {
        'firstname': 'Kris',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 5
    },
    {
        'firstname': 'Bob',
        'Group': 42,
        'physics': 9,
        'informatics': 5,
        'history': 8
    },
    {
        'firstname': 'Tom',
        'Group': 42,
        'physics': 2,
        'informatics': 4,
        'history': 5
    }
]


def statistic(pupils):
    out_information = []
    subjects = ['physics', 'informatics', 'history']
    for i in pupils:
        sum_rate = 0
        for key, value in i.items():
            if key in subjects:
                sum_rate += value
        if sum_rate / len(subjects) >= 4:
            out_information.append(i)
    for i in out_information:
        print(i)


statistic(pupils)
