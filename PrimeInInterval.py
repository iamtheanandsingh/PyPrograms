x = int(input("Enter The Number Till You Want To Find Primes : "))

for i in range(1, x+1):
    count = 0
    for j in range(1, i+1):
        if j % i == 0 : 
            count += 1

    if (count == 1):
        print("\n", j)