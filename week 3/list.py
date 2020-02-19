alist=[1, 42, "Hello"]
for x in alist[-2:]:  #x goes through all members of alist
    print(x)

blist=[1,2,3,4,5]
blist=blist+[1,2,3,4,5]
blist[9]=8
for x in blist:
    print(x)
