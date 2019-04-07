def add3no(a, b, c):
    return a + b + c


#print("Addition of given no is " + str(add3no(2, 3, 4)))

result = add3no(2, 3, 4)
#print(result)


def hello(name):
    print("hello " + name)


hello("Amol")


def hi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
    print("Hello {}! You are {} years old.".format("Amol", 30))


hi("Amol", 30)

