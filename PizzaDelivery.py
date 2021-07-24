#Making A Pizza bill Program!

print("\nWelcome To Pizzaz!!")

size = input("\nEnter Size S/M/L : ")

pep = input("Add Pepperoni? Y/N : ")
cheese = input("Add Cheese? Y/N : ")

#Small Pizza
if size == 's' or size == 's':
    if pep == 'Y' or pep == 'y':
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $18")
        else:
            print("\nBill Is $17")
    else:
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $16")
        else:
            print("\nBill Is $15")

#Medium Pizza
elif size == 'm' or size == 'M':
    if pep == 'Y' or pep == 'y':
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $24")
        else:
            print("\nBill Is $23")
    else:
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $21")
        else:
            print("\nBill Is $20")

#Large Pizza
elif size == 'L' or size == 'l':
    if pep == 'Y' or pep == 'y':
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $29")
        else:
            print("\nBill Is $28")
    else:
        if cheese == 'y' or cheese == 'y':
            print("\nBill Is $26")
        else:
            print("\nBill Is $25")
else:
    print("\nEnter Valid Choice!")

print("\nThank You For Eating With Us!")