x = int(input("\nEnter Range Of List 1 : "))
y = int(input("\nEnter Range Of List 2 : "))

l1 = []
l2 = []

print("\nEnter List 1 : ")

for i in range(0,x):
    z = int(input())
    l1.append(z)

print("\nEnter List 2 : ")

for i in range(0,y):
    w = int(input())
    l2.append(w)

print("\nList 1 Is :")
print(l1)

print("\nList 2 Is :")
print(l2)

l1.extend(l2)

print("\nExtended List 1 Is : ")
print(l1)