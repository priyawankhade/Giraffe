secretWord = "Password"
guessWord = ""
guessCount = 0
guessLimit = 3
outofGuess = False

while secretWord != guessWord and not outofGuess:
    if guessCount < guessLimit:
        guessWord = input("Enter guess word: ")
        guessCount += 1
    else:
        outofGuess = True


if outofGuess:
    print("Better Luck Next Time.")
else:
    print("Congrats! You won!")
