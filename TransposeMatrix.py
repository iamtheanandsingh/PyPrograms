x = int(input("Enter Rows : "))
y = int(input("Enter Columns : "))

arr = []

for i in range(0,x):
    for j in range(0,y):
        z = input()
        arr.append(z)

result = []

for i in range(0,y):
    for j in range(0,x):
        result[i][j] = arr[i][j]