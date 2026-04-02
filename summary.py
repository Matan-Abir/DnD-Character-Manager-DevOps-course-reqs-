def display_summary_menu(characters):
    print(f"\n{'=+='*20}")
    print(f"{'=+='*9} SUMMARY {'=+='*8}")
    print(f"{'=+='*20}")
    print(f"\nNumber of characters: {len(characters)}")

def summary_main_loop(characters):
    is_active = True
    while is_active:
        display_summary_menu(characters)
        input("Press any key to return to main menu... ")
        is_active = False
        pass
    pass