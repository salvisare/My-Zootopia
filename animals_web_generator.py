import json

def load_data(animals_data):
  with open("animals_data.json", "r") as handle:
    return json.load(handle)


def restructure_data(data):
  for item in data:
    if "name" in item:
      print(f"Name: {item["name"]}")
    if 'characteristics' in item:
      characteristics = item["characteristics"]
      if "diet" in characteristics:
        print(f"Diet: {characteristics["diet"]}")
    if "locations" in item:
      locations = item['locations']
      location_string = ', '.join(locations)
      print(f"Location: {location_string}")
    if 'characteristics' in item:
      characteristics = item["characteristics"]
      if "type" in characteristics:
        print(f"Type: {characteristics["type"]}")
    print("")

animals_data = load_data("animals_data.json")

print(restructure_data(animals_data))