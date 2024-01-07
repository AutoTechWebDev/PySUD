import random
import os
from PySUD_character_races import races  # Import the race dictionary

# Function to roll all dice needed:
def rd4():
    return random.randint(1, 4)
def rd6():
    return random.randint(1, 6)
def rd8():
    return random.randint(1, 8)
def rd10():
    return random.randint(1, 10)
def rd12():
    return random.randint(1, 12)
def rd20():
    return random.randint(1, 20)


      

# Function for character creation
def create_character():
    # Initialize an empty character dictionary
    character = {
        "Name": "",
        "Class": "",
        "Race": "",
    }
    abilities = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }


################################################################################################################################################################################
#Begin Character Creation
    print("Welcome to ... character creation!")
    character["Name"] = input("Enter your character's name: ")
    


###############################################################################################################################################################################
    # Choosing a class
    print("\nChoose your class:")
    print("1. Sorcerer")
    print("2. Wizard")
    print("3. Artificer")
    print("4. Bard")
    print("5. Cleric")
    print("6. Druid")
    print("7. Monk")
    print("8. Rogue")
    print("9. Warlock")
    print("10. Fighter")
    print("11. Paladin")
    print("12. Ranger")
    print("13. Barbarian")

    class_choice = input("Enter the number of your chosen class: ")

    if class_choice == "1":
        character["Class"] = "Sorcerer"
    elif class_choice == "2":
        character["Class"] = "Wizard"
    elif class_choice == "3":
        character["Class"] = "Artificer"
    elif class_choice == "4":
        character["Class"] = "Bard"
    elif class_choice == "5":
        character["Class"] = "Cleric"
    elif class_choice == "6":
        character["Class"] = "Druid"
    elif class_choice == "7":
        character["Class"] = "Monk"
    elif class_choice == "8":
        character["Class"] = "Rogue"
    elif class_choice == "9":
        character["Class"] = "Warlock"
    elif class_choice == "10":
        character["Class"] = "Fighter"
    elif class_choice == "11":
        character["Class"] = "Paladin"
    elif class_choice == "12":
        character["Class"] = "Ranger"
    elif class_choice == "13":
        character["Class"] = "Barbarian"
    else:
        print("Invalid choice. Defaulting to Sorcerer.")
        character["Class"] = "Sorcerer"


###############################################################################################################################################################################
    # Choosing a race
    print("\nChoose your race:")
    print("1. Dwarf")
    print("2. Elf")
    print("3. Halfling")
    print("4. Human")
    race_choice = input("Enter the number of your chosen race: ")

    if race_choice == "1":
        character["Race"] = "Dwarf"
    elif race_choice == "2":
        character["Race"] = "Elf"
    elif race_choice == "3":
        character["Race"] = "Halfling"
    elif race_choice == "4":
        character["Race"] = "Human"   
    else:
        print("Invalid choice. Defaulting to Human.")
        character["Race"] = "Human" 
        
    if race_choice in races:
        character["Race"] = races[race_choice]['name']  # Set the chosen race

        # Check if the chosen race has subraces
        if races[race_choice]['subraces']:
            print(f"Choose your subrace for {character['Race']}:")
            for sub_index, subrace in races[race_choice]['subraces'].items():
                print(f"{sub_index}. {subrace['name']}")

            subrace_choice = input("Enter the number of your chosen subrace or type 'none': ")

            if subrace_choice in races[race_choice]['subraces']:
                character["Subrace"] = races[race_choice]['subraces'][subrace_choice]['name']
            elif subrace_choice.lower() == 'none':
                character["Subrace"] = "None"  # Set the subrace to 'None'
            else:
                print("Invalid subrace choice. Defaulting to standard race.")
                character["Subrace"] = "None"  # Set the subrace to 'None' as default

        else:
            print("Invalid choice. Defaulting to Human.")
            character["Race"] = "Human"
            character["Subrace"] = "None"  # Set the subrace to 'None' for the default race


###############################################################################################################################################################################
    #Rolling Ability Scores         
    print("\nRolling ability scores...")
    


    # Roll three sets of dice for each ability
    rolls_sets = {ability: [sorted([rd6() for _ in range(3)], reverse=True) for _ in range(3)] for ability in abilities}
    for ability, rolls in rolls_sets.items():
        print(f"{ability} Rolls:")
        for i, rolls_set in enumerate(rolls):
            print(f"Set {i + 1}: {rolls_set}")

    # Let the player choose from the three sets for each ability
    for ability in abilities:
        while True:
            choice = input(f"Choose the set for {ability} (1, 2, or 3): ")
            if choice in ["1", "2", "3"]:
                abilities[ability] = sum(rolls_sets[ability][int(choice) - 1][:3])  # Assign the sum of the three rolls
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


###############################################################################################################################################################################
   # Displaying the created character
    print("\nCharacter created!")
    print(f"\nName: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Race: {character['Race']}")
    print(f"SubRace: {character['Subrace']}")
    for ability, score in abilities.items():
        print(f"{ability}: {score}")
    print(f"Good luck {character['Name']} ")

# Create a character using create_character()
    
    return character, abilities   

character, abilities = create_character()


def save_character(character, abilities):
    # Combine character and abilities
    character_with_abilities = character.copy()
    character_with_abilities["Abilities"] = abilities
    
    # Get the directory of the current Python file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(current_directory, "players")
    
    filename = f"{character['Name']}.txt"
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, "w") as file:
            file.write(f"Character: {character['Name']}\n")
            for key, value in character_with_abilities.items():
                if key != 'Name' and isinstance(value, dict):
                    file.write(f"{key}:\n")
                    for k, v in value.items():
                        file.write(f"  {k}: {v}\n")
                elif key != 'Name':
                    file.write(f"{key}: {value}\n")
        print(f"Character and abilities saved to '{file_path}'")
    except Exception as e:
        print(f"Error occurred while saving character: {e}")

# Check if character is valid before saving
if character:
    save_character(character, abilities)
else:
    print("Character creation failed or returned None.")


