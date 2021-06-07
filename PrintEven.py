x = int(input("\n Enter Number Of Elements In Array :"))

arr = []

print("\n Enter Elements Of Array : \n")

for i in range(0,x):
    y = int(input("Enter Value : "))
    arr.append(y)

print("The Number Of Even Elements In Array : ")

for i in range(0,x):
    if arr[i] %2 == 0:
        print(arr[i],"\t")