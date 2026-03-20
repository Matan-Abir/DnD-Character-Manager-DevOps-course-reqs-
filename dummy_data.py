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

def override_with_dummy_data(characters):
    characters = dummy_data.copy()
    return characters

def append_with_dummy_data(characters):
    characters.append(dummy_data)
    return characters

def dummy_data_main_loop(characters):
    inp = int(input("press 1 to overwrite, 2 to append"))
    print(f"input is {inp}")
    if inp == 1:
        print("chosen to override")
        return override_with_dummy_data(characters)
    if inp == 2:
        print("chosen to append")
        return append_with_dummy_data(characters)
    if inp != 1 and inp != 2:
        print("WRONG!")