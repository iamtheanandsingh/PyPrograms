x = int(input("Enter Number :"))

count = 0

for i in range(1,x):
    if x%i == 0:
        count+=1

if count == 1:
    print("Prime!")
else:
    print("Not Prime!")