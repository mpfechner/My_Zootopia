import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
  """ Loads a HTML file """
  with open(file_path, "r") as handle:
    return handle.read()

animals = load_data('animals_data.json')
template = load_template('animals_template.html')
output = ''
for entry in animals:
    name = entry.get("name")
    diet = entry.get("characteristics", {}).get("diet")
    locations = entry.get("locations")
    animal_type = entry.get("characteristics", {}).get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if locations and len(locations) > 0:
        print(f"Location: {locations[0]}")
    if animal_type:
        print(f"Type: {animal_type}")

    print("-" * 20)  # Trenner für Übersicht

