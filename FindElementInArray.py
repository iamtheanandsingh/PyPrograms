def find(arr, t, x):
    for i in range (0,x):
        if arr[i] == t:
            return i

x = int(input("\n Enter Number Of Elements In Array : "))

arr = []

print("Enter Array Elements : ")
for i in range(0,x):
    y = int(input())
    arr.append(y)

t = int(input("Enter Target : "))

z = find(arr, t, x)

if z:
    print("Target Found At Index", i)
else:
    print("Sorry! The Target Is Not In The Array! T_T")