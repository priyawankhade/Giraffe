a = 5
i = 1
while i <= 10:
    #print(a * i)
    i += 1
#print("Loop completed.")

i = 1
while i <= 10:
    #print(i)
    i += 1


#GuessingWord:

secretWord = "Password"
guess = ""
guessCount = 0
guessLimit = 3
outofGuess = False

while guess != secretWord and not outofGuess:
    if guessCount < guessLimit:
        guess = input("Enter Guess: ")
        guessCount += 1
    else:
        outofGuess = True

if outofGuess:
    print("You Lose")

else:
    print("You Win!")








