data = 'Sasha 43, Masha 23'
age = ''
names = ''
for i in data:
    for j in i:
        if j.isdigit():
            age += j
sasha_age = int(age[0:2])
masha_age = int(age[2:4])
for a in data.split(' '):
    if a.istitle():
        names += a

name_sasha=names[:5]
name_masha=names[5:]
print(f"{names[:5]} {sasha_age}, {names[5:]} {masha_age} ")
