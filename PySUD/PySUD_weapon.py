# WEAPON INFORMATION BELOW HERE
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    # Example weapons
weapon1 = Weapon(name="Sword", damage=15)
weapon2 = Weapon(name="Dagger", damage=10)
weapon3 = Weapon(name="Staff", damage=12)
weapon4 = Weapon(name="Hammer", damage=18)
weapon5 = Weapon(name="Bow", damage=14)

class WarriorWeapon(Weapon):
    pass

    # Magic weapons for Warrior
warrior_magic_weapons = [
    WarriorWeapon(name="Flaming Blade", damage=20),
    WarriorWeapon(name="Thunderstrike Axe", damage=18),
    WarriorWeapon(name="Vorpal Sword", damage=22),
    WarriorWeapon(name="Frostbite Maul", damage=25),
    WarriorWeapon(name="Inferno Halberd", damage=23)
]

    # Rare weapons for Warrior
warrior_rare_weapons = [
    WarriorWeapon(name="Titanium Cleaver", damage=28),
    WarriorWeapon(name="Obsidian Bastard Sword", damage=30),
    WarriorWeapon(name="Dragonbone Greatsword", damage=32),
    WarriorWeapon(name="Mjolnir", damage=35),
    WarriorWeapon(name="Executioner's Blade", damage=31)
]

    # Unique weapons for Warrior
warrior_unique_weapons = [
    WarriorWeapon(name="Excalibur", damage=40),
    WarriorWeapon(name="Soulrender", damage=45),
    WarriorWeapon(name="Aegisbane", damage=50),
    WarriorWeapon(name="Blade of the Phoenix", damage=55),
    WarriorWeapon(name="Doombringer", damage=60)
]

class RogueWeapon(Weapon):
    pass

# Magic weapons for Rogue
rogue_magic_weapons = [
    RogueWeapon(name="Venomous Dagger", damage=18),
    RogueWeapon(name="Shadowstrike Blades", damage=20),
    RogueWeapon(name="Silent Shiv", damage=16),
    RogueWeapon(name="Blade of Disguise", damage=22),
    RogueWeapon(name="Viper Fangs", damage=24)
]

# Rare weapons for Rogue
rogue_rare_weapons = [
    RogueWeapon(name="Assassin's Blade", damage=28),
    RogueWeapon(name="Nightshade Knives", damage=30),
    RogueWeapon(name="Death's Whisper", damage=32),
    RogueWeapon(name="Cloak and Dagger", damage=26),
    RogueWeapon(name="Serrated Stiletto", damage=35)
]

# Unique weapons for Rogue
rogue_unique_weapons = [
    RogueWeapon(name="Eclipse Edge", damage=40),
    RogueWeapon(name="Whisperwind Blades", damage=45),
    RogueWeapon(name="Shadowstep Scimitars", damage=50),
    RogueWeapon(name="Phantom Blade", damage=55),
    RogueWeapon(name="Deadly Deception", damage=60)
]

class WizardWeapon(Weapon):
    pass

# Magic weapons for Wizard
wizard_magic_weapons = [
    WizardWeapon(name="Arcane Staff", damage=16),
    WizardWeapon(name="Fireball Wand", damage=18),
    WizardWeapon(name="Frostbite Scepter", damage=20),
    WizardWeapon(name="Thunderbolt Rod", damage=22),
    WizardWeapon(name="Eldritch Orb", damage=24)
]

# Rare weapons for Wizard
wizard_rare_weapons = [
    WizardWeapon(name="Spellweaver Staff", damage=28),
    WizardWeapon(name="Blizzard Cane", damage=30),
    WizardWeapon(name="Tome of Elements", damage=32),
    WizardWeapon(name="Chaos Focus", damage=26),
    WizardWeapon(name="Celestial Wand", damage=35)
]

# Unique weapons for Wizard
wizard_unique_weapons = [
    WizardWeapon(name="Staff of the Archmage", damage=40),
    WizardWeapon(name="Scepter of Sorcery", damage=45),
    WizardWeapon(name="Astral Conduit", damage=50),
    WizardWeapon(name="Eternal Staff", damage=55),
    WizardWeapon(name="Primordial Grimoire", damage=60)
]

class PaladinWeapon(Weapon):
    pass

# Magic weapons for Paladin
paladin_magic_weapons = [
    PaladinWeapon(name="Holy Mace", damage=18),
    PaladinWeapon(name="Divine Hammer", damage=20),
    PaladinWeapon(name="Blessed Sword", damage=16),
    PaladinWeapon(name="Zealot's Blade", damage=22),
    PaladinWeapon(name="Radiant Lance", damage=24)
]

# Rare weapons for Paladin
paladin_rare_weapons = [
    PaladinWeapon(name="Avenger's Flail", damage=28),
    PaladinWeapon(name="Heaven's Defender", damage=30),
    PaladinWeapon(name="Justicebringer", damage=32),
    PaladinWeapon(name="Guardian's Edge", damage=26),
    PaladinWeapon(name="Exorcist's Maul", damage=35)
]

# Unique weapons for Paladin
paladin_unique_weapons = [
    PaladinWeapon(name="Lionheart Blade", damage=40),
    PaladinWeapon(name="Sword of Virtue", damage=45),
    PaladinWeapon(name="Divinity's Call", damage=50),
    PaladinWeapon(name="Exalted Warhammer", damage=55),
    PaladinWeapon(name="Redemption's Edge", damage=60)
]

class ArcherWeapon(Weapon):
    pass

# Magic weapons for Archer
archer_magic_weapons = [
    ArcherWeapon(name="Swift Bow", damage=18),
    ArcherWeapon(name="Poisoned Arrows", damage=20),
    ArcherWeapon(name="Hailstorm Crossbow", damage=16),
    ArcherWeapon(name="Eagle Eye Longbow", damage=22),
    ArcherWeapon(name="Serpent's Fang", damage=24)
]

# Rare weapons for Archer
archer_rare_weapons = [
    ArcherWeapon(name="Marksman's Rifle", damage=28),
    ArcherWeapon(name="Stormcaller Bow", damage=30),
    ArcherWeapon(name="Recurve Bow", damage=32),
    ArcherWeapon(name="Soulfire Crossbow", damage=26),
    ArcherWeapon(name="Venomstrike Bow", damage=35)
]

# Unique weapons for Archer
archer_unique_weapons = [
    ArcherWeapon(name="Windrider Bow", damage=40),
    ArcherWeapon(name="Skyward Arrows", damage=45),
    ArcherWeapon(name="Predator's Crossbow", damage=50),
    ArcherWeapon(name="Frostbite Longbow", damage=55),
    ArcherWeapon(name="Dragon's Breath", damage=60)
]
