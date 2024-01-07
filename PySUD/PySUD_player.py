import random
from PySUD_character_races import races  # Import the race dictionary
from PySUD_character_creation import create_character #Import the character created

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






# PLAYER INFORMATION BELOW HERE!!!

#Define player "class" or "role"
class Sorcerer(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d6", average_value=4)

class Wizard(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d6", average_value=4)

class Artificer(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Bard(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Cleric(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Druid(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Monk(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Rogue(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Warlock(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Fighter(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Paladin(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Ranger(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Barbarian(PlayerDetails):
    def __init__(self):
        super().__init__(hit_dice="d12", average_value=7)

#Define all player attributes/stats
class PlayerDetails:
    # Initialize Player Values
    def __init__(self, character, health=100, hit_dice, average_value, inventory=None):
        self.role = role 
        self.name = {character['Name']}
        self.race = {character['Race']}
        self.health = health + self.calculate_health()
        self.level = 1
        self.hit_dice = hit_dice
        self.average_value = average_value
        self.inventory = inventory if inventory else []
        self.experience = 0
        self.experience_to_next_level = 100  # Example threshold to reach next level


        #Set hit_dice and average_value based on the characters class
        role = character['Class']
        if role in self.HIT_DICE_VALUES:
            self.hit_dice = self.HIT_DICE_VALUES[role]["hit_dice"]
            self.average_value = self.HIT_DICE_VALUES[role]["average_value"]
        else:
            # Set default values for other classes if needed
            self.hit_dice = "d8"  # Default hit_dice for other classes
            self.average_value = 5  # Default average_value for other classes

    def calculate_health(self):
        if self.hit_dice == "d6":
            return self.level * 4  # Health increase by 4 per level for d6
        elif self.hit_dice == "d8":
            return self.level * 5  # Health increase by 5 per level for d8
        elif self.hit_dice == "d10":
            return self.level * 6  # Health increase by 6 per level for d10
        elif self.hit_dice == "d12":
            return self.level * 7  # Health increase by 7 per level for d12

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = calculate_next_level_experience(self.level)
        self.apply_level_benefits()

    def calculate_next_level_experience(current_level):
    # Example function to calculate the experience required for the next level
        return 100 + (current_level * 50)

    def apply_level_benefits(self):
        # Apply benefits of leveling up (e.g., increase health, unlock skills)
        pass

    














#Player Actions Below Here
    #Defining player movement
    def move(self, direction):
        if direction in self.current_room.exits:
            # Update the player's current_room attribute
            next_room_name = self.current_room.exits[direction]
            self.current_room = dungeon_map[next_room_name]  # Assuming dungeon_map holds all rooms
            print("You move to", self.current_room.description)
        else:
            print("You can't go that way.")
    #Defining picking up items/taking items
    def take_item(self, item_name):
        if item_name in self.current_room.items:
            # Remove the item from the room and add it to the player's inventory
            self.current_room.items.remove(item_name)
            self.inventory.append(item_name)
            print("You take the", item_name)
        else:
            print("There's no", item_name, "here.")
    #Defining using items/equipping items
    def use_item(self, item_name):
        if item_name in self.inventory:
            # Check the item and perform corresponding action
            if item_name == 'health_potion':  # Example item action (healing)
                self.health += 20  # Assuming a health potion heals 20 points
                self.inventory.remove(item_name)
                print("You used the health potion and gained 20 health.")
            # Add more item actions as needed
            else:
                print("You can't use the", item_name, "right now.")
        else:
            print("You don't have a", item_name, "in your inventory.")
    #Definining attacking monsters
    def attack(self, monster):
        if self.current_room.monster == monster:
            # Perform an attack on the specified monster
            # Here, assuming a simple combat scenario
            monster_health = monster.health  # Assuming 'monster' has a health attribute
            player_damage = 20  # Player's damage per attack

            # Reduce monster's health based on player's attack
            monster_health -= player_damage

            # Update monster's health attribute (assuming 'monster' is an object with health attribute)
            monster.health = monster_health

            print("You attacked the", monster.name, "and dealt", player_damage, "damage.")

            if monster.health <= 0:
                print("You defeated the", monster.name)
                # Perform actions for defeating the monster (e.g., remove it from the room)
                self.current_room.monster = None  # Assuming the monster disappears after defeat
        else:
            print("There's no", monster.name, "to attack here.")

class Sorcerer(Player):
    def __init__(self):
        super().__init__(hit_dice="d6", average_value=4)

class Wizard(Player):
    def __init__(self):
        super().__init__(hit_dice="d6", average_value=4)

class Artificer(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Bard(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Cleric(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Druid(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Monk(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Rogue(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Warlock(Player):
    def __init__(self):
        super().__init__(hit_dice="d8", average_value=5)

class Fighter(Player):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Paladin(Player):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Ranger(Player):
    def __init__(self):
        super().__init__(hit_dice="d10", average_value=6)

class Barbarian(Player):
    def __init__(self):
        super().__init__(hit_dice="d12", average_value=7)

player1 = Player(name="Warrior", health=100)
player2 = Player(name="Rogue", health=80)
player3 = Player(name="Wizard", health=70)
player4 = Player(name="Paladin", health=110)
player5 = Player(name="Archer", health=90)
