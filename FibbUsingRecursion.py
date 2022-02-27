def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
        
nterms = int(input("Enter The Number Of Terms : "))

if nterms < 0:
    print("Enter Natural Number.")
else:
    print("Fibonacci Sequence Is : ")
    for i in range (nterms):
        print(fibo(i))