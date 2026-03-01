#Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?

A= int(input("Enter your speed km/h: "))
B= int(input("Enter your speed km/hr: "))
C= int(input("Enter your speed km/hr: "))

avg= (A+B+C)//3

print("The average speed is",avg)

if A<avg:
    print("Cycist A is riding slower than the average speed")
if B<avg:
    print("Cyclist B is riding less than the aveage speed.")
if C<avg:
    print ("Cyclist C is riding slower than average speed")


