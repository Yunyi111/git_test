def getvalues(n):
    #pretend nothing was found here (from a database)
    return None

#call the function

student_number=1234

if getvalues(student_number)==None:
    print("Student not found")
else:
    print("Student found")