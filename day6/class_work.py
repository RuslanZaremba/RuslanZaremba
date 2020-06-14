import json


def dict_data(data1, data2, data3):
    spis_keys = []
    spis_keys.extend(data1.keys())
    spis_keys.extend(data2.keys())
    spis_keys.extend(data3.keys())
    spis_values = []
    spis_values.extend(data1.values())
    spis_values.extend(data2.values())
    spis_values.extend(data3.values())
    data = {}
    for i in range(len(spis_keys)):
        data[spis_keys[i]] = spis_values[i]
    return data


data1 = {'name': 'sasha'}
data2 = {'last_name': 'Viktorov'}
data3 = {'sur_name': 'Ivaov'}

with open('myfile.txt', 'w') as myfile:
    di = dict_data(data1, data2, data3)
    print(json.dumps(di))

with open('myfile.txt') as myfile:
    line = json.loads(myfile)
    print(line)
