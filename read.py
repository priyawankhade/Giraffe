try:
    tablefile = open("/Users/bhatkarmohan/Documents/Test.java", "r")
    if tablefile.readable():
        for table in tablefile.readlines():
            print(table)

    tablefile.close()
except FileNotFoundError as err:
    print(err)
