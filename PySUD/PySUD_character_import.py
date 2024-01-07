import os

def import_character(file_path):
    character = {}
    abilities = {}

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            for line in lines:
                parts = line.split(": ")
                if len(parts) == 2:
                    key, value = parts
                    key = key.strip()
                    value = value.strip()

                    if key == "Character:":
                        character["Name"] = value
                    elif key == "Character Attributes:":
                        continue  # Skip this line
                    else:
                        character[key] = value

                        # Check if the line indicates abilities
                        if ":" in value:
                            ability, score = value.split(": ")
                            abilities[ability] = int(score)

            print("Character and abilities imported successfully.")
            return character, abilities

    except FileNotFoundError:
        print("File not found.")
        return None, None

# Input file location
file_location = input("Enter the file location to import the character from: ")

# Check if the file exists
if os.path.exists(file_location):
    character, abilities = import_character(file_location)
else:
    print("File does not exist. Please provide a valid file location.")
#C:\Users\Eternal\Desktop\Programming\PySUD\players\Collezio.txt