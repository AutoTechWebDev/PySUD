from PySUD_character_creation import create_character, save_character

# Create a character using create_character()
character = create_character()

# Check if character is valid before saving
if character:
    save_character(character)
else:
    print("Character creation failed or returned None.")