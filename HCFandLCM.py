def hcf(num1, num2):
    if num1> num2:
        less = num2
    else:
        less = num1
    for i in range(1, less+1):
        if num1%i == 0 and num2%i==0:
            hcf = i

def lcm(lcm1, lcm2):
    t = lcm1 * lcm2
    for j in range(0, t + 1):
        if j%lcm1==0 and j%lcm2==0:
            lcm = j

x = int(input("Enter A : "))
y = int(input("Enter B : "))

hcf(x,y)
lcm(x,y)

print("HCF Of Numbers Is : ", hcf)
print("LCM Of Numbers Is : ", lcm)