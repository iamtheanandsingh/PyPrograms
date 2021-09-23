import math
import random

caps = 'abcdefghijklmnopqrstuwxyz'
smol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb = '!@#$%^&*()-_+=\][}{|":;?><,./'
numb = '1234567890'

x = int(input("Enter The Number Of Characters You Want : "))

st = caps + smol + symb + numb

pas = ""

for i in range(0,x):
    pas+=random.choice(st)
print("Your Password Is : ", pas)