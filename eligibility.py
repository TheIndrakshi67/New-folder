medicalcause=input("Do you have a medical cause?")

if medicalcause=="Yes":
    print("Allowed")
else:
    attendance=float(input("Enter attendence percentage: "))
    if attendance>75:
        print("Allowed")
    else:
        print("Not allowed")