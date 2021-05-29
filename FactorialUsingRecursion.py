def fact (num):
    if num == 1:
        return num
    else:
        return (num*fact(num-1))

x = int(input("Enter Number : "))

print("The Factorial Of The Entered Number Is : ", fact(x))