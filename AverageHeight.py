x = int(input("Enter Number Of Entries : "))

arr = []

for i in range(0,x):
    z = int(input("Enter Height : "))
    arr.append(z)

c = 0

for i in range(0,x):
    c += arr[i]

print("The Average Of Heights Are : ", c/x)