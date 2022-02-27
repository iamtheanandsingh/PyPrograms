
num1 = int(input("Please enter the first value number 1 : "))
num2 = int(input("Please enter the second value number 2 : "))

a=num1
b=num2
Icm=0

while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp

gcd=num1
Icm=((a*b)/gcd)

print("\n HCF of ",a,"and",b,"=",gcd)
print("\n LCM of ",a,"and",b,"=",Icm)