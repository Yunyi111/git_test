while True:
    input_number=input("your number >")
    result=int(input_number)%2
    print("the number is ", end="") #don't change a line, continue in this line
    if result==0:
        print("even")
    else:
        print("odd")
    confirmation=input("would you like to continue? (y/n) >")
    if confirmation=="n":
        break



