x = int(input("Enter A : "))
y = int(input("Enter B : "))
z = int(input("Enter C : "))

maxi = 0

print("The Max Of 3 Numbers Is : ")

#Method One
print("\n 1. The Hard Way")
print("\t Using if-else Construct \n")

if x > y and x > z:
    maxi = x
elif y > x and y > z:
    maxi = y
else:
    maxi = z

print("Maximum Of A, B And C Is : ", maxi)

#Method Two 
print("\n 2. The Easy Way")
print("\t Using max() Function \n")

print("Maximum Of A, B And C Is : ", max(x, y, z))