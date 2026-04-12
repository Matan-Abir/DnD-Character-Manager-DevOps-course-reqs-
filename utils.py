"""
Allows for navigation in menus via numbers.
"""

def menu_nav_input_numeral(lowest, highest):
    nav_input = input("\nUser Input: ")
    try:
        nav_input = int(nav_input)
        if nav_input >= lowest and nav_input <= highest:
            return nav_input
        print(f"\nInput must be between {lowest} and {highest}!\n")
        input("Press enter to continue...")
        return -1
    except Exception:
        print("\nInput has to be a whole number!\n")
        input("Press enter to continue...")
        return -1

"""
Used to see what values are valid in menu navigation.

Args:
    options (enum): The available options in any menu. Every module with navigation has this.

Returns:
    lowest (int): The lowest valid number in menu navigation (usually 0 or 1).
    highest (int): The highest valid number in menu navigation.
"""
def get_enum_highest_lowest(options):
    all_enum_values = [option.value for option in options]
    all_enum_values.sort()
    lowest, highest = all_enum_values[0],all_enum_values[-1]
    return lowest, highest

"""
The method used for handling input when creating a character's stats.
"""
def check_stat_input_validity(stat_name):
    stat = -1
    is_valid = False
    print("\nCharacter stats should be between 1 and 20.")
    while True:
        stat_input = input(f"\nPlease input character's {stat_name}: ")
        try:
            stat = int(stat_input)
            if stat > 20 or stat < 1:
                print(f"\n{stat} is not within the bounds of 1 and 20!\n")
            else:
                is_valid = True
        except ValueError:
            print("You must enter a number!")
        if is_valid:
            break
    return stat

"""
Used to prevent the user from entering empty strings during inputs
"""
def non_empty_input(input_text):
    finished_input = False
    while (not finished_input):
        user_input = input(input_text)
        if user_input != "":
            return user_input
        input("\nYou have to enter some text to proceed. Press enter to try again..\n")