x = int(input("\nEnter Range Of List : "))

l1 = []

print("\nEnter List : ")

for i in range(0,x):
    z = int(input())
    l1.append(z)

l1.reverse()

print("The Reverse Of The List Is : ", l1)