from enum import IntEnum
from display import display_character
import utils

class Update_Menu_Options(IntEnum):
    EXIT = 0
    UPDATE_NAME = 1
    UPDATE_LEVEL = 2
    UPDATE_RACE = 3
    UPDATE_CLASS = 4
    UPDATE_STATS = 5
    UPDATE_INVENTORY = 6

lowest, highest = utils.get_enum_highest_lowest(Update_Menu_Options)

"""
Changes a character's name.
"""
def update_character_name(character):
    print(f"Current character name: {character['name']}")
    character['name'] = input("What would you like this character's new name to be? Input new name: ")

"""
Changes a character's level.
"""
def update_character_level(character):
    print(f"Current character level: {character['level']}")
    character['level'] = input("What would you like this character's new level to be? Input new level: ")

"""
Changes a character's race.
"""
def update_character_race(character):
    print(f"Current character race: {character['race']}")
    character['race'] = input("What would you like this character's new race to be? Input new race: ")

"""
Changes a character's class.
"""
def update_character_class(character):
    print(f"Current character clas: {character['class']}")
    character['class'] = input("What would you like this character's new class to be? Input new class: ")

"""
Changes a character's stats.
"""
def update_character_stats(character):
    stats = character['stats']
    print(f"Current character stats: \nSTR: {stats['str']}\tDEX: {stats['dex']}\tCON: {stats['con']}")
    print(f"INT: {stats['int']}\tWIS: {stats['wis']}\tCHA: {stats['cha']}")
    
    stats['str'] = utils.check_stat_input_validity("strength")
    stats['dex'] = utils.check_stat_input_validity("dexterity")
    stats['con'] = utils.check_stat_input_validity("constitution")
    stats['int'] = utils.check_stat_input_validity("intelligence")
    stats['wis'] = utils.check_stat_input_validity("wisdom")
    stats['cha'] = utils.check_stat_input_validity("charisma")

"""
Changes a character's inventory.
"""
def update_character_inventory(character):
    inventory = character['inventory']
    is_active = True
    while (is_active):
        try:
            print(f"{character['name']}'s inventory has the following items:")
            counter = 1
            for item in inventory:
                print(f"{counter}. {item}")
                counter += 1
            print("\nChoose item index to remove, press N to add a new item or 0 to finish updating items.")
            inventory_choice = input("User Choice: ")
            if inventory_choice == "N":
                new_item = input("Enter new item to be added: ")
                inventory.append(new_item)
            elif inventory_choice == "0":
                is_active = False
            elif int(inventory_choice) > 0 and int(inventory_choice) < (len(inventory)):
                input(f"Deleting {inventory[int(inventory_choice)-1]}, press Enter to continue")
                del inventory[int(inventory_choice)-1]
            else:
                input("Invalid input, press enter to try again")
        except IndexError:
            print(f"Input must be N (capital letter) or between 0 and {len(inventory)}")

"""
Displays a specific character's update menu.
"""
def display_character_update_menu(character):
    print("\nDisplaying character info:")
    display_character(character)
    print("\nPress 1 to update name")
    print("Press 2 to update level")
    print("Press 3 to update race")
    print("Press 4 to update class")
    print("Press 5 to update stats")
    print("Press 6 to update inventory")
    print("Press 0 to return to character choice menu")


"""
Displays the update menu.
"""
def display_update_menu(characters):
    print(f"{"="*100}")
    print("="*40,"Update Characters","="*41)
    print("="*100,"\n\n")
    print("Choose a character to update by entering its number!")
    print("0. Return to Main Menu")
    counter = 1
    for character in characters:
        print(f"{counter}. {character['name']}, level {character['level']} {character['race']} {character['class']}")
        counter += 1

#########################
# Update Menu Main Loop #
#########################

def update_menu_main_loop(characters):
    is_active = True
    while(is_active):
        try:
            display_update_menu(characters)
            character_choice = input("\nPlease choose a character to update: ")
            character_number = int(character_choice)
            if (character_number == 0):
                is_active = False
                continue
            display_character_update_menu(characters[character_number-1])
            chosen_character = characters[character_number-1]
            nav_input = utils.menu_nav_input_numeral(lowest, highest)
            match nav_input:
                case Update_Menu_Options.UPDATE_NAME:
                    update_character_name(chosen_character)
                case Update_Menu_Options.UPDATE_LEVEL:
                    update_character_level(chosen_character)
                case Update_Menu_Options.UPDATE_RACE:
                    update_character_race(chosen_character)
                case Update_Menu_Options.UPDATE_CLASS:
                    update_character_class(chosen_character)
                case Update_Menu_Options.UPDATE_STATS:
                    update_character_stats(chosen_character)
                case Update_Menu_Options.UPDATE_INVENTORY:
                    update_character_inventory(chosen_character)
                case Update_Menu_Options.EXIT:
                    input("Returning to main update menu. Press Enter to continue...")
                    pass
        except ValueError:
            print("You must enter a number!")
            input("Press enter to try again..")
        except IndexError:
            print("You must enter a number within range!")
            input("Press enter to try again..")