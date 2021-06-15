def con(num):
    if num > 1:
        con(num//2)
    print(num % 2,end = '')

x = int(input("Enter Decimal : "))

con(x)