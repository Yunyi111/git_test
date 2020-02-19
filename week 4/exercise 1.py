mylist=list(range(0,11))

newlist=[]
for a in mylist:
    x=pow(2,a) #pow(value,exponent)
    newlist.append(x)

print(newlist)


mylist=[pow(2,x) for x in range (0,11)]
print(mylist)