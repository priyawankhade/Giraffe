isTall = True
isMale = True
isMarried = True

if isTall and isMale and isMarried:
    print("You are tall , married male.")

elif isTall and isMale and not isMarried:
    print("You are tall married male. ")

elif isTall and not isMale and isMarried:
    print("You are tall, married but are not male.")

elif isTall and not isMale and not isMarried:
    print("You are tall, unmarried but are not male. ")

elif not isTall and isMale and isMarried:
    print("You are short male and are married.")

elif not isTall and isMale and not isMarried:
    print("You are short, unmarried male.")

elif not isTall and not isMale and isMarried:
    print("You are short, married but are not male.")

else:
    print("You are neither tall nor male and nor married.")
