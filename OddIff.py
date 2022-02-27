#Function to check if a number isodd or even

def oddcheck(number):
    if number%2 == 0:
        print("Entered Number Is Even")
    else:
        print("Entered Number Is Odd")

x = int(input("Enter Number : "))

oddcheck(x)