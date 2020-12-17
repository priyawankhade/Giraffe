#This prpgram is for file reading!

file = open("fileops.txt", "r")
for name in file.readlines():
    print(name)



