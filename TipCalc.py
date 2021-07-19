def tip(bill):
    tips = 0
    y = int(input("Enter % Tip You Want To Give (10, 12, 15) : "))
    if y == 10:
        tips = (bill*10)/100
        return tips
    elif y == 12:
        tip = (bill*12)/100
        return tips
    elif y == 15:
        tip = (bill*15)/100
        return tips
    else:
        print("Enter Only Acceptable Values!")

print("Welcome To Tip Calculator!")

x = float(input("Total Bill : $"))

t = tip(x)

tot = x + t

z = int(input("How Many Will Split The Bill? : "))

each = round(tot/z, 2)

print("Each Person Should Pay : $", each)