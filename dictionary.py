airportName = {
    "BOM": "Mumbai",
    "DL": "Delhi",
    "HND": "Haneda",
    "NRT": "Narita"

}

print(airportName["HND"])
print(airportName.get("DL"))
print(airportName.get("jgf", "Not a valid key."))


keylist = list(airportName.keys())
valuelist = list(airportName.values())

print(keylist[valuelist.index("Mumbai")])


def findkey(val):
    for key, value in airportName.items():
        if val == value:
            return key
    return "Key not found."


print(findkey("Mumbai"))
