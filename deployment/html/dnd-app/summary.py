# I didn't really have much to do with this module considering the nature
# of the program but here you go I guess

"""
The method for displaying the summary menu
"""
def display_summary_menu(characters):
    print(f"\n{"=+="*20}")
    print(f"{"=+="*9} SUMMARY {"=+="*8}")
    print("=+="*20)
    print(f"\nNumber of characters: {len(characters)}")

"""
Main loop for the summary menu.
"""
def summary_main_loop(characters):
    is_active = True
    while is_active:
        display_summary_menu(characters)
        input("Press any key to return to main menu... ")
        is_active = False
        pass
    pass