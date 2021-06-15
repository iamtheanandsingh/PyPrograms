#printing factorial of a number

x = int(input("Enter The Number Till Factorial Is Wanted : "))

fact = 1

for i in range(1,x+1):
    fact *= i

print("Factorial Of", x, "Is :", fact)