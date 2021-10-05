def check(num):
    if num>18 or num==18:
        print("You Are Eligible To Vote. Congratulations!")
    else:
        print("Sadly, You Cannot Vote. Wait Till You Come Of Age.")

x = int(input("Enter Age : "))

check(x)