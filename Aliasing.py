import random

x = int(input("\nEnter Range Of List 1 : "))

l1 = []

print("\nEnter List 1 : ")

for i in range(0,x):
    z = int(input())
    l1.append(z)

l2 = l1

r = random.randint(0,x-1)

t = int(input("\nEnter Change In A Random Element : "))

l2[r] = t

print("\nAfter Aliasing\n\nList 2 :  ", l2)
print("\nList 1 :",l1)