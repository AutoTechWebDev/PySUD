#DWARF
class Dwarf:
    def __init__(self):
        self.traits = {
            "Ability Score Increase": "Your Constitution score increases by 2.",
            "Age": "Dwarves mature at the same rate as humans, but they’re considered young until they reach the age of 50. On average, they live about 350 years.",
            "Alignment": "Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.",
            "Size": "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.",
            "Speed": "Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.",
            "Darkvision": "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.",
            "Dwarven Resilience": "You have advantage on saving throws against poison, and you have resistance against poison damage.",
            "Dwarven Combat Training": "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.",
            "Tool Proficiency": "You gain proficiency with the artisan’s tools of your choice: smith’s tools, brewer’s supplies, or mason’s tools.",
            "Stonecunning": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check.",
            "Languages": "You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.",
            "Subraces": ["Hill Dwarf", "Mountain Dwarf"]
        }

class HillDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Wisdom score increases by 1."
        self.traits["Dwarven Toughness"] = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."

class MountainDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Strength score increases by 2."
        self.traits["Dwarven Armor Training"] = "You have proficiency with light and medium armor."

# Example usage:
# Creating a Dwarf character
dwarf = Dwarf()
hill_dwarf = HillDwarf()
mountain_dwarf = MountainDwarf()

# Accessing Hill Dwarf traits
#print("Hill Dwarf Traits:")
#for trait, description in hill_dwarf.traits.items():
    #print(f"{trait}: {description}")



# Accessing Mountain Dwarf traits
    #print("\nMountain Dwarf Traits:")
    #for trait, description in mountain_dwarf.traits.items():
        #print(f"{trait}: {description}")












#ELF
class Elf:
    def __init__(self):
        self.traits = {
            "Ability Score Increase": "Your Dexterity score increases by 2.",
            "Age": "Elves mature at a slower rate than humans. They reach adulthood around the age of 100 and can live to be over 700 years old.",
            "Alignment": "Elves tend to be chaotic, valuing personal freedom. They lean towards good due to their compassion.",
            "Size": "Elves range from under 5 to over 6 feet tall and have a slender build. Your size is Medium.",
            "Speed": "Your base walking speed is 30 feet.",
            "Darkvision": "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
            "Fey Ancestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "Trance": "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. You can dream during this meditation, gaining the same benefits as a human does from 8 hours of sleep.",
            "Languages": "You can speak, read, and write Common and Elvish.",
            "Subraces": ["High Elf", "Wood Elf"]
        }

class HighElf(Elf):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Intelligence score increases by 1."
        self.traits["Elf Weapon Training"] = "You have proficiency with the longsword, shortsword, shortbow, and longbow."
        self.traits["Cantrip"] = "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."

class WoodElf(Elf):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Wisdom score increases by 1."
        self.traits["Elf Weapon Training"] = "You have proficiency with the longsword, shortsword, shortbow, and longbow."
        self.traits["Fleet of Foot"] = "Your base walking speed increases to 35 feet."
        self.traits["Mask of the Wild"] = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."

# Example usage:
# Creating instances of Elf and its subraces
elf = Elf()
high_elf = HighElf()
wood_elf = WoodElf()

# Accessing traits for Elf and its subraces
    #print("Elf Traits:")
    #for trait, description in elf.traits.items():
        #print(f"{trait}: {description}")

    #print("\nHigh Elf Traits:")
    #for trait, description in high_elf.traits.items():
        #print(f"{trait}: {description}")

    #print("\nWood Elf Traits:")
    #for trait, description in wood_elf.traits.items():
        #print(f"{trait}: {description}")










#Halfling
class Halfling:
    def __init__(self):
        self.traits = {
            "Ability Score Increase": "Your Dexterity score increases by 2.",
            "Age": "A halfling reaches adulthood in their early twenties and generally lives into the middle of their second century.",
            "Alignment": "Halflings tend to be lawful good. They value the comforts of home and hearth over adventuring.",
            "Size": "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is Small.",
            "Speed": "Your base walking speed is 25 feet.",
            "Lucky": "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.",
            "Brave": "You have advantage on saving throws against being frightened.",
            "Halfling Nimbleness": "You can move through the space of any creature that is of a size larger than yours.",
            "Languages": "You can speak, read, and write Common and Halfling.",
            "Subraces": ["Lightfoot", "Stout"]
        }

class Lightfoot(Halfling):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Charisma score increases by 1."
        self.traits["Naturally Stealthy"] = "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."

class Stout(Halfling):
    def __init__(self):
        super().__init__()
        self.traits["Ability Score Increase"] += " Your Constitution score increases by 1."
        self.traits["Stout Resilience"] = "You have advantage on saving throws against poison, and you have resistance against poison damage."

# Example usage:
# Creating instances of Halfling and its subraces
halfling = Halfling()
lightfoot = Lightfoot()
stout = Stout()

# Accessing traits for Halfling and its subraces
    #print("Halfling Traits:")
    #for trait, description in halfling.traits.items():
        #print(f"{trait}: {description}")

    #print("\nLightfoot Traits:")
    #for trait, description in lightfoot.traits.items():
        #print(f"{trait}: {description}")

    #print("\nStout Traits:")
    #for trait, description in stout.traits.items():
        #print(f"{trait}: {description}")






#HUMAN
class Human:
    def __init__(self):
        self.traits = {
            "Ability Score Increase": "Your ability scores each increase by 1.",
            "Age": "Humans reach adulthood in their late teens and can live less than a century.",
            "Alignment": "Humans tend to be very diverse in alignment due to their varied cultures and personalities.",
            "Size": "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Your size is Medium.",
            "Speed": "Your base walking speed is 30 feet.",
            "Languages": "You can speak, read, and write Common and one extra language of your choice.",
            "Subrace": "Variant (if applicable)"
        }

class VariantHuman(Human):
    def __init__(self):
        super().__init__()
        self.traits["Skills and Feat"] = "You gain proficiency in one skill of your choice and gain one feat of your choice."

# Example usage:
# Creating instances of Human and its variant
human = Human()
variant_human = VariantHuman()

# Accessing traits for Human and its variant
    #print("Human Traits:")
    #for trait, description in human.traits.items():
        #print(f"{trait}: {description}")

    #print("\nVariant Human Traits:")
    #for trait, description in variant_human.traits.items():
        #print(f"{trait}: {description}")





races = {
    "1": {
        "name": "Dwarf",
        "class": dwarf,
        "subraces": {
            "1": {
                "name": "Hill Dwarf",
                # Other attributes of the Hill Dwarf subrace
                "class": hill_dwarf,
            },
            "2": {
                "name": "Mountain Dwarf",
                # Other attributes of the Mountain Dwarf subrace
                "class": mountain_dwarf,
            },
            # More subraces for Dwarves if available
                     },
        # Other attributes of the Dwarf race
            },
    "2": {
        "name": "Elf",
        "class": elf,
        "subraces": {
            "1": {
                "name": "High Elf",
                "class": high_elf,
                # Other attributes of the High Elf subrace
            },
            "2": {
                "name": "Wood Elf",
                "class": wood_elf,
                # Other attributes of the Wood Elf subrace
            },
            # More subraces for Elves if available
                },
                # Other attributes of the Elf race
            },
    "3": {
        "name": "Halfling",
        "class":  halfling,
        "subraces": {
            "1": {
                "name": "Lightfoot Halfling",
                "class": lightfoot,
                # Other attributes of the Lightfoot Halfling subrace
            },
            "2": {
                "name": "Stout Halfling",
                "class": stout,
                # Other attributes of the Stout Halfling subrace
            },
            # More subraces for Halflings if available
                },
                # Other attributes of the Halfling race
            },
    "4": {
        "name": "Human",
        "class": human,
        "subraces": {
            "1": {
                "name": "Varient",
                "class": variant_human,
                # Other attributes of the Lightfoot Halfling subrace
                    },
                },
    # More races and their respective subraces if available
            }
}