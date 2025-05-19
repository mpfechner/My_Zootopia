import json
from typing import Any, Dict, List


def load_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load animal data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: A list of animal data entries.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(file_path: str) -> str:
    """
    Load HTML template from a file.

    Args:
        file_path (str): Path to the HTML template file.

    Returns:
        str: The contents of the HTML template.
    """
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal: Dict[str, Any]) -> str:
    """
    Convert a single animal's data into an HTML snippet.

    Args:
        animal (Dict[str, Any]): A dictionary representing the animal.

    Returns:
        str: HTML string representing the animal.
    """
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")
    distinctive_feature = animal.get("characteristics", {}).get("distinctive_feature")

    animal_data = '<li class="cards__item">'
    if name:
        animal_data += f'<div class="card__title">{name}</div>'
    animal_data += '<ul>'
    if diet:
        animal_data += f'<p class="card__text"><li><strong>Diet:</strong>: {diet}</li></p>'
    if locations:
        animal_data += f'<p class="card__text"><li><strong>Location:</strong>: {locations[0]}</li></p>'
    if animal_type:
        animal_data += f'<p class="card__text"><li><strong>Type:</strong>: {animal_type}</li></p>'
    if distinctive_feature:
        animal_data += f'<p class="card__text"><li><strong>Distinctive feature:</strong>: {distinctive_feature}</li></p>'
    animal_data += '</ul></li>'

    return fix_encoding_issues(animal_data)


def fix_encoding_issues(text: str) -> str:
    """
    Fix common encoding issues in the text.

    Args:
        text (str): Input string that may contain unwanted characters.

    Returns:
        str: Cleaned string.
    """
    return text.replace("’", "'")


def write_template(text: str) -> bool:
    """
    Write the final HTML content to a file.

    Args:
        text (str): The HTML content to write.

    Returns:
        bool: True if successful.
    """
    with open("animals.html", "w") as handle:
        handle.write(text)
    return True


def main() -> None:
    """
    Main entry point of the script. Loads data, processes it,
    inserts it into the HTML template, and writes the result.
    """
    animals = load_data('animals_data.json')
    template = load_template('animals_template.html')
    output = ''.join(serialize_animal(entry) for entry in animals)

    final_output = template.replace("__REPLACE_ANIMALS_INFO__", output)
    if write_template(final_output):
        print("File written successfully")
    else:
        print("Error writing file")


if __name__ == '__main__':
    # Execute the main function only when the script is run directly.
    main()
