mylist=[4,5,10,20,10,54,22,1,20,20]

#requirement 1:
# get the lowest value
#requirement 2
# get the highest value
#requirement 3
# print a list of duplicated numbers

min=mylist[0]
max=mylist[0]

for x in mylist:

    #min
    if x<min:
        min=x
    #max
    if x>max:
        max=x

print(min)
print(max)




