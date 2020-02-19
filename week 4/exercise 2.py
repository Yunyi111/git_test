mylist=["A","B","C"]

copied_list_1=mylist

copied_list_2=mylist.copy()

mylist[1]="X"

print(mylist==copied_list_1)
print(mylist==copied_list_2)
