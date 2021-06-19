x = int(input("\nEnter Range Of List : "))

l1 = []

print("\nEnter List : ")

for i in range(0,x):
    z = int(input())
    l1.append(z)

print("\nList 1 Is :")
print(l1)

t = int(input("Enter What To Remove By Seeing The Entered List : "))

l1.remove(t)

print("The List After Removal Of The Element Is : ", l1)