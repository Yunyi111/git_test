a=input("what is your age?")
a=int(a)
b=input("Are you Male or Female?")
c=b[0].upper()
if a<20 and c=="M":
    print("you are qualified.")
else: print("you are not qualified.")
