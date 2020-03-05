student_number=input("Enter your student number >")

if (len(student_number)<8):
    raise Exception("Sorry the student number must be 8 digits long.")