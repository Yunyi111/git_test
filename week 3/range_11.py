limit=4

#draw a box

#method 1 (universal method)
for a in range(int(limit)):
    for b in range(int(limit)):
        print("*", end="")  #hotizontal
    print()  #vertical

#method 2 (more for Python)
for a in range(limit):
    print("#"*limit)

#draw a right-sided tiangle
for a in range(limit):
    print("$"*(a+1))  #when a=0, would print a blank line
