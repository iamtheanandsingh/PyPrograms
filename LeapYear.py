def ly(num):
    if num%4==0 and num%100!=0 or num%400==0:
        print("Leap Year Boss!")
    else: 
        print("Not A Leap Year Man!")

yr = int(input("Enter Year : "))
ly(yr)