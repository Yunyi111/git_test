def deposit(amount:float):

    assert (amount>0), "sorry the amount deposited must be greater than 0."

value=input("Enter an amount to deposit >")

try:
    deposit(float(value))
except AssertionError as error_text:
    print("error_text")

except Exception as error_text:
    print("an unhandled error has occurred: "+str(error_text))

else:  #if no error occurred
    print("If no error has occurred, run these lines.")
    #send email of confirmation of deposit here.