import utils
from random import randrange
from enum import IntEnum

class Add_Menu_Options(IntEnum):
    EXIT = 0
    ADD_CHARACTER = 1

"""
Creates the stats dictionary and assigns it the values from character creation

Args:
    stats (list): A list of 6 stats

Returns:
    dictionary: a dict of 6 stats
"""
def create_stats(stats):
    stats_dict = {}
    stats_dict['str'] = stats[0]
    stats_dict['dex'] = stats[1]
    stats_dict['con'] = stats[2]
    stats_dict['int'] = stats[3]
    stats_dict['wis'] = stats[4]
    stats_dict['cha'] = stats[5]
    return stats_dict

"""
Creates the stats for a character randomly by summing three
random numbers between 1 and 6 for each stat

Returns: 
    list: 6 random stats
"""
def randomize_stats():
    stats = []
    for i in range(6):
        stats.append(randrange(1,7) + randrange(1,7) + randrange(1,7))
    return create_stats(stats)


"""
Manual inputs for the 6 stats with validity checks
"""
def manual_stats_input():
    stats = []
    stats.append(utils.check_stat_input_validity("strength"))
    stats.append(utils.check_stat_input_validity("dexterity"))
    stats.append(utils.check_stat_input_validity("constitution"))
    stats.append(utils.check_stat_input_validity("intelligence"))
    stats.append(utils.check_stat_input_validity("wisdom"))
    stats.append(utils.check_stat_input_validity("charisma"))
    return create_stats(stats)

"""
Display the "Add Character" menu
"""

def display_add_main_menu():
    print(f"\n{"="*100}")
    print("="*40,"Character Creation","="*40)
    print("="*100,"\n\n")
    print("Enter 1 to create a new character, or 0 to return to main menu!")
    print("1. Create New Character")
    print("0. Back To Main Menu")

"""
A looping menu for adding inventory items for characters
"""
def add_inventory_items(inventory):
    is_active = True
    while (is_active):
        if (inventory): # if inventory has items
            print(f"\nCurrent inventory: {", ".join(inventory)}")
        else:
            print("\nInventory currently has no items in it.")
        print("\nPress 1 to enter another inventory item, or 0 to finish")
        inventory_choice = input("Choice: ")
        if inventory_choice == '1':
            print("Enter new item: ")
            item = input("")
            inventory.append(item)
        elif inventory_choice == '0':
            print("Finalizing inventory creation..")
            input("Press enter to progress..")
            is_active = False
        else:
            print("You can only input 1 or 2 in this menu. Please try again.")
            input("Press enter to try again.")
    
    return inventory
    
"""
Create the character

Args:
    name (string): The character's name
    level (int): The character's level
    race (string): The character's race
    character_class (string): the character's class
    stats (dictionary): A dictionary of the 6 stats
    inventory (list): A list of the character's items

Returns:
    character: The "character" object
"""
def finalize_character(name, level, race, character_class, stats, inventory):
    character = {}
    character['name'] = name
    character['level'] = level
    character['race'] = race
    character['class'] = character_class
    character['stats'] = stats
    character['inventory'] = inventory
    return character

"""
Create a character.
"""
def create_character():
    print("\nWhat is the new character's name? ")
    name = utils.non_empty_input("Name: ")
    print("\nWhat is the new character's level? ")
    level_invalid = True
    while level_invalid:
        try:
            level = input("Level: ")
            level_as_int = int(level)
            if level_as_int < 1:
                input("Level must be 1 or higher!")
            else: 
                level_invalid = False
        except:
            input("You must enter a number!")
    print("\nWhat is the new character's race? ")
    race = utils.non_empty_inputinput("Race: ")
    print("\nWhat is the new character's class? ")
    character_class = utils.non_empty_inputinput("Class: ")
    stats = None
    print("\nWhat is the new character's stats? ")
    print("Press 1 to manually input, 2 for randomization.")
    random_choice = input("Choice: ")
    if (int(random_choice) != 1 
    and int(random_choice) != 2):
        print("\nChoice has to be 1 or 2. Defaulting to random.")
        stats = randomize_stats()
    else:
        if int(random_choice) == 1:
            stats = manual_stats_input()
        else:
            stats = randomize_stats()
    inventory = []
    inventory = add_inventory_items(inventory)
    return finalize_character(name, level, race, character_class, stats, inventory)
    


lowest, highest = utils.get_enum_highest_lowest(Add_Menu_Options)


######################
# Add Menu Main Loop #
######################

def add_menu_main_loop(characters):
    is_active = True
    while (is_active):
        display_add_main_menu()
        nav_input = utils.menu_nav_input_numeral(lowest, highest)
        match nav_input:
            case Add_Menu_Options.ADD_CHARACTER:
                print("\nAdding Character!")
                input("Press enter to continue.. ")
                new_character = create_character()
                characters.append(new_character)
            case Add_Menu_Options.EXIT:
                print("Quitting to main menu...")
                input("Press enter to continue..\n")
                is_active = False