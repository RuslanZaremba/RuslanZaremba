import json

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

# ЗАПИСЬ JSON DUMP

# with open('my_first_json_dump.json', 'w') as first:
#     json.dump(to_json, first, sort_keys=True, indent=2)
# with open('my_first_json_dump.json') as first:
#     print(first.read())
#
# # ЗАПИСЬ JSON DUMPS
#
# with open('my_first_json_dumps.json', 'w') as second:
#     second.write(json.dumps(to_json, sort_keys=True, indent=2))
#
# with open('my_first_json_dumps.json') as first:
#     print(first.read())

# ЧТЕНИЕ JSON LOAD

with open('my_first_json_dump.json') as file:
    templates = json.load(file)
print(type(templates), templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

# ЧТЕНИЕ JSON LOADS

# with open('my_first_json_dumps.json') as dump:
#     file_content = dump.read()
#     templates = json.loads(file_content)
# print(templates)
#
# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
