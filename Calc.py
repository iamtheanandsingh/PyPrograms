def add(a,b):
    print("A+B = ", a+b)

def sub(a,b):
    print("A-B = ", a-b)

def mul(a,b):
    print("A*B = ", a*b)

def div(a,b):
    print("A/B = ", a/b)

x = int(input("Enter A : "))
y = int(input("Enter B : "))

print("\n Choose From One : \n 1. Add \n 2. Sub \n 3. Multiply \n 4. Divide \n")
t = int(input("Enter Choices 1/2/3/4 : "))

if t == 1:
    add(x, y)
elif t == 2:
    sub(x, y)
elif t == 3:
    mul(x, y)
elif t == 4:
    div(x, y)
else:
    print("Enter Number In Range.")


#This Is A Simple Calculating Python App.