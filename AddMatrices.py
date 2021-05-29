R = int(input("Enter The Number Of Rows : "))
C = int(input("Enter The Number Of Columns : "))

A = []
B = []

print("Enter The Entries Row-Wise : ")

print("\n Enter Martix A : ")

for i in range(R):		
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	A.append(a)

print("\n Enter Martix B : ")

for i in range(R):		
	b = []
	for j in range(C):	 
		b.append(int(input()))
	B.append(b)

result = []

for i in range(0, R):
   for j in range(0, C):
       result[i][j] = A[i][j] + B[i][j]

for r in result:
   print(r)