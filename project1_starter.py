"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Nariyah White]
Date: [10/31/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

"""
Creates a new character dictionary with calculated stats
Returns: dictionary with keys: name, class, level, strength, magic, health, gold

Example:
char = create_character("Aria", "Mage")
# Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
"""
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
#level = 1 #every level has to start at level 1

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    if character_class == "Warrior":
        strength = 10 + (level - 1) * 3
        magic = 2 + (level - 1)
        health = 20 + (level - 1) * 5
    elif character_class == "Mage":
        strength = 3 + (level - 1)
        magic = 10 + (level - 1) * 4
        health = 12 + (level - 1) * 3
    elif character_class == "Rogue":
        strength = 7 + (level - 1) * 2
        magic = 6 + (level - 1) * 2
        health = 10 + (level - 1) * 2
    elif character_class == "Cleric":
        strength = 6 + (level - 1) * 2
        magic = 9 + (level - 1) * 3
        health = 18 + (level - 1) * 4
    elif character_class not in ["Warrior", "Mage", "Rogue", "Cleric"]:
        print("Error: Invalid character class. Stats not calculated")
        strength = 0
        magic = 0
        health = 0
    return strength, magic, health

def create_character(name, character_class):
    valid_class = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_class:
        print("Error: Invaild character class. Character not created.")
        return None
    level = 1
    strength, magic, health = calculate_stats(character_class, level)


    character = {
            "name": name,
            "class": character_class,
            "level": level,
            "strength": strength,
            "magic": magic,
            "health": health,
            "gold": 100
        }
    return character


def save_character(character, filename):
    directory = os.path.dirname(filename)

    if directory and not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return False


    with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
    return True


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    if not os.path.exists(filename):
        print("Error: File '{filename}' not found.")
        return None

    with open(filename, "r") as file:
        lines = file.readlines()
        character = {}
        for line in lines:
            if ": " in line:
                key, value = line.strip().split(": ")
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)
            return character



def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the c\
    haracter dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    character["level"] += 1
    character["strength"], character["magic"], character["health"] = calculate_stats(character["class"],
                                                                                     character["level"])
    character["gold"] += 50
    print(f"{character['name']} has leveled up to level {character['level']}!")


# Main program area (optional - for testing your functions)
#if __name__ == "__main__":
    #print("=== CHARACTER CREATOR ===")
   # print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
