value=input("provide an integer >")

try:
    num=int(value)
    print(num*10)

except Exception as e:
    print("an exception has occurred "+str(e))

