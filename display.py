import utils
from math import floor

class Display_Menu_Options(utils.MenuOption):
     EXIT = 0, "Back To Main Menu"
     DISPLAY_ALL = 1, "Display All Characters"
     DISPLAY_BY_LEVEL = 2, "Display All Characters (Sorted Descending by Level)"
     DISPLAY_BY_KEYWORD = 3, "Display All Characters (Filtered By Keyword)"

lowest, highest = utils.get_enum_highest_lowest(Display_Menu_Options)

def display_display_menu():
     print("="*100)
     print("="*41,"Character Display","="*40)
     print("="*100,"\n\n")
     print("Choose a feature to use by entering its number!")
     utils.print_menu_options(Display_Menu_Options)

def display_all_characters(characters):
     for character in characters:
          display_character(character)

def display_character(character):
    print(f"\nName: {character['name']}")
    print(f"{character['race']} {character['class']}")
    print(f"Level: {character['level']}")
    stats = character['stats']
    print(f"Strength: {stats['str']} ({floor((stats['str']-10)/2)})")
    print(f"Dexterity: {stats['dex']} ({floor((stats['dex']-10)/2)})")
    print(f"Constitution: {stats['con']} ({floor((stats['con']-10)/2)})")
    print(f"Intelligence: {stats['int']} ({floor((stats['int']-10)/2)})")
    print(f"Wisdom: {stats['wis']} ({floor((stats['wis']-10)/2)})")
    print(f"Charisma: {stats['cha']} ({floor((stats['cha']-10)/2)})")
    if dict.get(character, 'inventory'):
         inventory = character['inventory']
         print("Inventory:")
         for item in inventory:
              print(f"-{item}")
    print("\n")

def display_characters_by_level(characters):
     sorted_characters = sorted(characters, key=lambda x: x["level"], reverse=True)
     display_all_characters(sorted_characters)

def display_characters_by_keyword(characters):
     result_list = []
     print("Please enter the keyword to search by: ")
     search_keyword = input()
     for character in characters:
          inventory = dict.get(character, 'inventory')
          if (search_keyword in dict.values(character) or
              search_keyword in dict.values(character['stats']) or
              (inventory is not None and search_keyword in inventory)): 
               result_list.append(character)
     if len(result_list) == 0:
          print(f"No characters matching the keyword {search_keyword} found!")
     else:
          for character in result_list:
               display_all_characters(result_list)

##########################
# Display Menu Main Loop #
##########################
def display_menu_main_loop(characters):
    is_active = True
    while (is_active):
        display_display_menu()
        nav_input = utils.menu_nav_input_numeral(lowest, highest)
        match nav_input:
             case Display_Menu_Options.DISPLAY_ALL:
                  display_all_characters(characters)
             case Display_Menu_Options.DISPLAY_BY_LEVEL:
                  display_characters_by_level(characters)
             case Display_Menu_Options.DISPLAY_BY_KEYWORD:
                  display_characters_by_keyword(characters)
             case Display_Menu_Options.EXIT:
                  print("\nExiting Display Menu...")
                  input("Press enter to continue...\n")
                  is_active = False