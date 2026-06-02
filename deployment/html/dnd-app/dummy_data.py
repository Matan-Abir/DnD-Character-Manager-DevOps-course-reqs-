# A good example of what a character structure looks like.
# Each character has a name, level, race, class, 6 stats (named str, dex, con, int, wis, cha)
# and an inventory, which is what items they have.
dummy_data = [
              {'name':'Matan','level':6,'race':'Human','class':'Warlock',
              'stats':{'str':8,'dex':9,'con':9,'int':13,'wis':15,'cha':18},
              'inventory':['Shrunken Head','Component Pouch']},
              {'name':'Kenji','level':20,'race':'Wood-Elf','class':'Samurai',
              'stats':{'str':20,'dex':23,'con':16,'int':12,'wis':15,'cha':11},
              'inventory':['Katana','Kabuto','Omamori Charm','Book of the Five Rings']},
              {'name':'Steve Jobs','level':14,'race':'Zombie','class':'Programmer',
              'stats':{'str':11,'dex':10,'con':6,'int':18,'wis':15,'cha':20},
              'inventory':['Gray Turtleneck','iPhone 4']},
              ]

"""
Overwrites the characters list with the dummy data characters.
"""
def override_with_dummy_data(characters):
    characters = dummy_data.copy()
    return characters

"""
Appends the dummy data characters to the characters list.
"""
def append_with_dummy_data(characters):
    characters.append(dummy_data)
    return characters

def dummy_data_main_loop(characters):
    option_chosen = False
    while (not option_chosen):
        try:
            inp = int(input("Debug menu! Press 1 to overwrite the character list, or 2 to append to it\n"))
            if inp == 1:
                input("Character list overwritten with dummy data! Press enter to return..")
                option_chosen = True
                return override_with_dummy_data(characters)
            if inp == 2:
                input("Character list appended with dummy data! Press enter to return..")
                option_chosen = True
                return append_with_dummy_data(characters)
        except:
            input("You can only input 1 or 2 in this menu. Press enter to try again.")