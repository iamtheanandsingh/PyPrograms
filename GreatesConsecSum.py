x = int(input())    #enter number to couple
y = int(input())    #enter number of array elements

arr = []

for i in range(0,y):
    d = int(input())
    arr.append(d)

count = []

for i in range(0,y-x):
    a = 0
    for j in range(i,i+x):
        a += x[j]
    count.append(a)

print(count.max())