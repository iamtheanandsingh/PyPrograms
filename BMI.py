def bmi(h,w):
    bm = (w/(h*h))*10000
    return bm

h = float(input("Enter The Height (in cm) :"))

w = float(input("Enter The Weight (in kg) :"))

bmx = round(bmi(h,w), 2)

if bmx < 18.5:
    print(f"You Are Underweight! Your BMI Is {bmx}.")
elif bmx >= 18.5 and bmx < 24.9:
    print(f"You Are Healthy! Your BMI Is {bmx}.")
elif bmx > 25 and bmx < 29:
    print(f"You Are Overweight! Your BMI Is {bmx}.")
else: 
    print(f"You Are Obese! Your BMI Is {bmx}")