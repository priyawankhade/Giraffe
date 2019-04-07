num1 = float(input("Enter first No.: "))
ope = input("Enter operation: ")
b = float(input("Enter second No.: "))

if ope == "+":
    print(num1 + b)

elif ope == "-":
    print(num1 - b)

elif ope == "*":
    print(num1 * b)

elif ope == "/":
    print(num1 / b)

else:
    print("Invalid Operation.")

