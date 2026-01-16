import math
print("-------------------------------------------------------")
print("I will find square root, log, and sine of your number.")
print("-------------------------------------------------------\n")

num = int(input("Please Enter your number: "))

sqrt = math.sqrt(num)
log = math.log(num)
sin = math.sin(num)

print("\nYour result is : ")
print(f"\n1.Square Root : {sqrt}\n2.Log : {log}\n3.sine : {sin}")
