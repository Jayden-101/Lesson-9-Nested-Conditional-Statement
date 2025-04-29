#Take input for the student that he can attend the exam or not 
medical_cause=input("did you have  a medical cause Y or N \n")
atten=int(input("enter the attendance of the student: "))


if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not Allowed")