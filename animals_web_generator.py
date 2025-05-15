import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
  """ Loads a HTML file """
  with open(file_path, "r") as handle:
    return handle.read()

def write_template(text):
    with open("animals.html", "w") as handle:
        handle.write(text)
    return True

animals = load_data('animals_data.json')
template = load_template('animals_template.html')
output = ''
for entry in animals:
    name = entry.get("name")
    diet = entry.get("characteristics", {}).get("diet")
    locations = entry.get("locations")
    animal_type = entry.get("characteristics", {}).get("type")

    output += '<li class="cards__item">'
    if name:
       output +=f"Name: {name}<br/>"
    if diet:
       output +=f"Diet: {diet}<br/>"
    if locations and len(locations) > 0:
       output +=f"Location: {locations[0]}<br/>"
    if animal_type:
       output +=f"Type: {animal_type}<br/>"
    output += '</li>'

template = template.replace("__REPLACE_ANIMALS_INFO__", output)
if write_template(template):
    print("File written successfully")
else:
    print("Error writing file")
exit()



