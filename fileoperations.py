file = open("fileops.txt", "w")
file.write("\n************************")
file.write("\nAmol - Software Engineer")
file.close()

file = open("fileops.txt", "a")
file.write("\nPriya - Awesome Software Engineer :)")
file.write("\n************************")
file.close()

file = open("fileops.txt", "r")
for f in file.readlines():
    print(f)
print(file.read())
file.close()

file = open("fileops.txt", "r")
for f in file.readline():
    print(f)









