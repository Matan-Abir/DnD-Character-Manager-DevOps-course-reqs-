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

def get_enum_highest_lowest(options):
    all_enum_values = [option.value for option in options]
    all_enum_values.sort()
    lowest, highest = all_enum_values[0],all_enum_values[-1]
    return lowest, highest

def check_stat_input_validity(stat_name):
    stat = -1
    is_valid = False
    print("Character stats should be between 1 and 20.")
    while True:
        stat_input = input(f"Please input character's {stat_name}: ")
        try:
            stat = int(stat_input)
            if stat > 20 or stat < 1:
                print(f"{stat} is not within the bounds of 1 and 20!")
            else:
                is_valid = True
        except ValueError:
            print("Value")
        if is_valid:
            break
    return stat