arr = []

x = int(input("Enter The Number Of Elements In Array : "))

for i in range(0,x):
    y = int(input())
    arr.append(y)

print("\n Entered Array Is : ", arr)

result = 0

for i in range(0,x):
    result = result + arr[i]

print("\n The Sum Of Elements In Array is", result)