a=int(input())
str=0
for m in range(a) :
 for n in range(12) :
    print("Data For Month %i Of Year %i"%(n,m))
    str+=int(input())


print("Total Inches Of Rainfall",str,"inches")
print("Total Months = ",12*a)
print("Avg. Rainfall/Month",str/(12*a),"in")