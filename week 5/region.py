#reading csv

import csv

region_units={}
region_revenue={}
regions=[]

current_region=""
current_units=0
current_revenue=0

f = open("region_input.csv", 'rt') #here use: with open..... as f:  >this is better way
reader = csv.reader(f)

#this is the header, we disregard it.
next(reader)

#read the input file

for row in reader:
    print(row) #temporary

    current_region=row[0]
    current_units=row[1]
    current_revenue=row[2]

#check dic to see if the current region exists

    if not current_region in region_units:
        region_units[current_region]=int(current_units)
    else:
        region_units[current_region]+=int(current_units)

regions=list(region_units.keys()) #have to put 'list'
print(regions)

print("All the regions found are: ", end="")
for r in regions:
    print(r, end=", ")
print() #to move to the next line

print("TOTALS PER REGION")
for r in regions:
    print(r)
    print("Total units for region: "+str(region_units[r]))
    print()











