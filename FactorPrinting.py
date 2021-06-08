def factor(num):
    for i in range (1, num):
        if num%i==0:
            print(i)

x = int(input("Enter Number : "))

print("The Factors Of The Entered Number Is : ")

factor(x)