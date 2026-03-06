print("Select your ride category ")
print( "1.Bike")
print("2.Car")
choice1= input ("Enter your choice(1 or 2): ")

if choice1=="1":
    print("You selected bike. Choose a subcategory.")
    print("1. Scooter")
    print("2. Sport bike")
    choice2= input("Enter you choice(1 or 2): ")
    if choice2=="1":
        print("Your ride is ready: Scooter")
    elif choice2=="2":
        print("Your ride is ready; A Sports Bike")
elif choice1=="2":
    print("You selected car. Choose a sub category")
    print("1. Sedan")
    print("2.SUV")
    choice2=input("Enter your choice(1 or 2): ")
    if choice2=="1":
     print("Your ride is ready: A Sedan")
    elif choice2=="2":
     print("Your ride is ready: A SUV")
