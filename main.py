import utils
from display import display_menu_main_loop
from add import add_menu_main_loop
from update import update_menu_main_loop
from summary import summary_main_loop
from dummy_data import dummy_data_main_loop

class Main_Menu_Options(utils.MenuOption):
    EXIT = 0, "Exit"
    DISPLAY = 1, "Display Characters"
    ADD = 2, "Add New Character"
    UPDATE = 3, "Update Existing Character"
    SUMMARY = 4, "Summary of Existing Characters"
    DUMMY = 5, "Load Dummy Data (Debug)"

def display_main_menu():
    print(f"\n{'=' * 100}")
    print("="*37,"Dungeons And Dragons 5E","="*38)
    print("="*37,"Character Tracking Tool","="*38)
    print("="*100,"\n\n")
    print("Choose a feature to use by entering its number!")
    utils.print_menu_options(Main_Menu_Options)


def exit_program():
    exit()

nav_input = -1
lowest, highest = utils.get_enum_highest_lowest(Main_Menu_Options)

characters = []

#####################
# Main Program Loop #
#####################
while (True):
    display_main_menu()
    nav_input = utils.menu_nav_input_numeral(lowest, highest)
    match nav_input:
        case Main_Menu_Options.DISPLAY:
            print("Entering Display Menu...")
            input()
            display_menu_main_loop(characters)
        case Main_Menu_Options.ADD:
            print("Entering Add Menu...")
            input()
            add_menu_main_loop(characters)
        case Main_Menu_Options.UPDATE:
            print("Entering Update Menu...")
            input()
            update_menu_main_loop(characters)
        case Main_Menu_Options.SUMMARY:
            print("Entering Summary Menu...")
            input()
            summary_main_loop(characters)
            pass
        case Main_Menu_Options.DUMMY:
            print("Loading dummy data...")
            input()
            characters = dummy_data_main_loop(characters)
            pass
        case Main_Menu_Options.EXIT:
            print("Exiting program. Goodbye!")
            input("Press enter to exit.\n")
            exit_program()