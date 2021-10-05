x = int(input())

arr = []

for i in range(0,x):
    d = int(input())
    arr.append(d)
    
maxx = 0

for i in range(0,x):
    if arr[i] > maxx:
        maxx = arr[i]
    
print(maxx)