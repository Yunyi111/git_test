first_list=list(range(1,11))
second_list=first_list.copy()  #built-in copy: list.copy()

print(first_list)
print(second_list)

second_list[2]=99

print(first_list)
print(second_list)

#manually do the copying
mylist3=[]
for val in second_list:
    mylist3.append(val)
print(mylist3)