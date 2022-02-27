a = 0
b = 1

x = int(input("Enter The Number Of Terms : "))

print("The Fibonacci Sequence Is : ")
print(a)
print(b)
for i in range (0, x - 2):
    c = a + b
    a = b
    b = c
    print(c)