inp = ""
while inp.upper()!="Q":
    inp=input("please enter a number")
    if int(inp)%10==0:
        print("number is divisible by 10")
    else:
        print("number is not divisible by 10")

