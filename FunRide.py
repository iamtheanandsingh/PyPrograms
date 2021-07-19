def photu(ph):
    if ph == 'Y' or ph == 'y':
        return True
    else:
        return False

x = int(input("Enter Your Height In cm : "))

print("Kid Tickets Are $5")
print("Teenager's Tickets Are $7")
print("Adult Tickets Are $12")

print("Enter ")

if x > 120:
    age = int(input("Enter Age : "))
    ph = input("Want A Photo? Y/N")
    z = photu(ph)

    if age > 18:
        if z == True:
            print("Bill = $15")
        else: 
            print("Bill = $12")
    elif age > 12 and age < 18:
        if z == True:
            print("Bill = $10")
        else: 
            print("Bill = $7")
    else: 
        if z == True:
            print("Bill = $8")
        else: 
            print("Bill = $5")