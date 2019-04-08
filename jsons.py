import json

handle = open("test.json", "r")
content = handle.read()

di = json.loads(content)

print(di["batters"]["batter"][1]["type"])

print(di["topping"][6]["type"])