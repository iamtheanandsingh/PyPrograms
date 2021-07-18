import random

n = random.randint(0, 10)

for i in range(0, 3):
    f = 2
    z = input("Want To Play A Game? Y/N : ")
    if f > -1:
        
        if z == 'Y' or z == 'y':
            
            if num > n:
                print("BZZZZ! Your Number Was Greater Than The Number!!")
                print("Missed! You Have %d Chances Left", f)
                
            elif num < n:
                print("BZZZZ! Your Number Was Lesser Than The Number!!")
                print("Missed! You Have %d Chances Left", f)
            
            else:
                print("Nigga. You Did It!")
                break
        
        elif z == 'n' or z == 'N':
            print("Thanks For Playing.")
    
    else :
        f -= i