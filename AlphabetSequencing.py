st = input("Enter String : ")

words = st.split()

words.sort()

print("The String In Order Is ")

for word in words:
    print(word)