fd = open("C:\\Users\iamth\Favorites\Python\\FileIO.txt", "w+")

fd.seek(4,0)

content = fd.read()

print(content)

fd.close()