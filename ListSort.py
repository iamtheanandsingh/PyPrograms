x = int(input("\nEnter Range Of List : "))

l1 = []

print("\nEnter List : ")

for i in range(0,x):
    z = int(input())
    l1.append(z)

print("\nEntered List Is :")
print(l1)

l1.sort()

print("\nSorted List Is : ", l1)