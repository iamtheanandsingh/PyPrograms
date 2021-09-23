x = int(input("Enter Rows : "))
y = int(input("Enter Columns : "))

arr1 = []
arr2 = []

for i in range(0,x):
    for j in range(0,y):
        z = input()
        arr1.append(z)

for i in range(0,x):
    for j in range(0,y):
        p = input()
        arr2.append(p)

res = []

for i in range(0, x):
    for j in range(0, y):
        for k in range(y):
           result[i][j] += X[i][k] * Y[k][j]