import json

obj = {a: 'aaa', b: 'bbb'}
obj_to_json = {'object': [obj]}
with open('text_files/text_15.json', 'w') as file:
    json.dump(obj, file)
