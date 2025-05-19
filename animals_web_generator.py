import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
  """ Loads a HTML file """
  with open(file_path, "r") as handle:
    return handle.read()


def serialize_animal(animal):
    animal_data = ""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")

    animal_data += '<li class="cards__item">'
    if name:
        animal_data += f'<div class="card__title">{name}</div>'
    if diet:
        animal_data += f"<strong>Diet:</strong>: {diet}<br/>"
    if locations and len(locations) > 0:
        animal_data += f"<strong>Location:</strong>: {locations[0]}<br/>"
    if animal_type:
        animal_data += f"<strong>Type:</strong>: {animal_type}<br/>"
    animal_data += '</li>'

    return fix_encoding_issues(animal_data)


def fix_encoding_issues(text):
    return text.replace("’", "'")



def write_template(text):
    with open("animals.html", "w") as handle:
        handle.write(text)
    return True


def main():
    animals = load_data('animals_data.json')
    template = load_template('animals_template.html')
    output = ''
    for entry in animals:
        output += serialize_animal(entry)

    template = template.replace("__REPLACE_ANIMALS_INFO__", output)
    if write_template(template):
        print("File written successfully")
    else:
        print("Error writing file")
    exit()

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    main()

