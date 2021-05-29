ls = []

x= int(input("\n Enter The Number Of Elements In The List : \n"))

for i in range(x):
    ls[i] = input()

print("\n The Entered List Is : \n")

for i in range(x):
    print(ls[i])

result = 1

for i in range(x):
    result = result * ls[i]

print("The Product Of The Elemens Are : ", result)