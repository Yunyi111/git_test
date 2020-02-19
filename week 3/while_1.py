inp=""
while True: #continue repeating, non-stop
    inp=input("enter a #")
    if inp.upper()=="Q":
        break
    if int(inp) % 10 == 0:
        print("number is divisible by 10")
    else:
        print("number is not divisible by 10")
