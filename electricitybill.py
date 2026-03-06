units= float(input("Enter number of units consumed: "))

if units<50:
    perunitcost=2.60
    tax=25
elif units<100:
    perunitcost=3.25
    tax=35
elif units<200:
    perunitcost=5.26
    tax=45
else:
    perunitcost=8.45
    tax=75

totalbill=(units*perunitcost)+tax

print("Total bill: ", totalbill)