# json  - {'name' : 'Radek"}
import json

person_dict = {"name": "Radek", "age": 40, "czy_pali": None}
print(person_dict)

with open('dane_nasze.json', 'w') as f:
    json.dump(person_dict, f)

# {"name": "Radek", "age": 40, "czy_pali": null}

with open('dane_nasze.json', 'r') as f:
    data = json.load(f)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}

print(data['name'])
print(data.keys())
print(data.values())
print(data.items())