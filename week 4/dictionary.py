d1={'us':'USA','ca':"Canada"}

d1['yy']='new country'
d1['yy']='Hello'

#print(d1['xx'])
print(d1.get('yy','not found'))
print(d1)


del d1['ca'] #same as: del d1[1]

for key, value in d1.items(): #specify key and value
    print(key, value)

for x in d1.keys():
    print(x)

for x in d1.values():
    print(x)

