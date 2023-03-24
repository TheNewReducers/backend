import json

with open("food_data.json", "r") as file:
    st = file.read()

    js = json.loads(st)

    print(js.keys())

