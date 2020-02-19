inp=""
mylist=[]    #need empty list

while True: #continue repeating, non-stop
    inp=input("enter a #")
    if inp.upper()=="Q":
        break

    mylist.append(int(inp))    # as long as not press Q, would add new# into the list

#if press Q
#to print sum of mylist
sum=0
for a in mylist:
    sum+=a

print(sum)

#to print average of mylist
average=sum/len(mylist)
print(average)


