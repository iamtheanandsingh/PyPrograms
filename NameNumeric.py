a=str(input())
sums=0
count=0
num=0
for i in a:
    sums=ord(i)+sums
if(sums%2==0):
    print("Numeric Value:",sums)
else:
    for i in range(2,sums):
        if(sums%i==0):
         count=count+1
    if(count==0):
        num=str(sums)
        if(len(num)==2):
            print("Numeric Value:",sums)
            print("lucky")
        else:
            print("Numeric Value:",sums)
            print("Unlucky")