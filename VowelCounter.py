vowels = 'aeiou'

str = input("\n Enter String : ")

str = str.casefold()

count = {}.fromkeys(vowels, 0)

for char in str:
    if char in count:
        count[char]+=1
    
print("\n The Numbers Of Vowels In The Entered String Is : ", count)