import random

def gamewin(comp, you):
    if comp == 1:
        if you == 2:
            return True
        elif you == 3:
            return False
    elif comp == 2:
        if you == 3:
            return True
        elif you == 1:
            return False
    elif comp == 3:
        if you == 2:
            return False
        elif you == 3:
            return True
    elif comp == you:
        return None
    else:
        print("Invalid!")

print("Enter A Number : \n1. Stone\n2. Paper \n3. Scissors\n")

you = int(input("Enter : "))
comp = random.randint(1,3)

print(f"\nComputer Chose {comp}")
print(f"You Chose {you}")

a = gamewin(comp, you)

if a == False:
    print("\nYou Lost T_T")
elif a == True:
    print("\nYou Win!!!")
else:
    print("\nIt's A Tie!")