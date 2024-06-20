import sys


class Character:
    def __init__(self, name, initiative, dexMod):
        self.name = name
        self.initiative = initiative
        self.dexMod = dexMod


initiative_tracker = []
test_mode = False

# For test/demo purposes, allow a command line arg to populate the order
if len(sys.argv) == 2 and sys.argv[1] == "test":
    test_mode = True
    initiative_tracker.append(Character("test1", 20, 0))
    initiative_tracker.append(Character("test2", 18, 1))
    initiative_tracker.append(Character("test3", 18, 2))
    initiative_tracker.append(Character("test4", 5, 1))
    initiative_tracker.append(Character("test5", 5, 2))
    initiative_tracker.append(Character("test6", 10, 0))


def main():
    clear()
    print("***Welcome to the Initiaive Tracker***")

    run = True
    while run == True:
        if test_mode == True:
            print("### Test Mode ###")

        command = instruction_query()

        match command:
            case "1":  # 1 Display current order
                clear()
                list_order()
                input()
            case "2":  # 2 Add a Character
                clear()
                add_char()
                input()
            case "3":  # 3 Change a characters initiative
                clear()
                update_init()
                input()
            case "4":  # 4 Remove a character from the initiative order
                clear()
                del_char()
                input()
            case "0":
                clear()
                print("Thank you for using the Initiative Tracker")
                run = False

        clear()


def list_order():
    print("*** CURRENT ORDER ***")
    sort_order()
    if len(initiative_tracker) > 0:
        for entry in initiative_tracker:
            print(f"{entry.name}: {entry.initiative} (mod: {entry.dexMod})")
    else:
        print("There are currently no characters in the initiative order.")


def sort_order():
    initiative_tracker.sort(key=lambda x: x.dexMod, reverse=True)
    initiative_tracker.sort(key=lambda x: x.initiative, reverse=True)


def instruction_query():
    print("Would you like to :")
    print("1. Display Current Order")
    print("2. Add a Character")
    print("3. Change a character's initiative")
    print("4. Remove a character from the initiative order")
    print("0. EXIT")

    in_number = input("Please enter the number of the option you'd like:")
    return in_number


def add_char():
    tempChar = input("Please enter a character name (required):")
    if not tempChar:
        print("Character name required. Returning to menu.")
        return

    tempInit = input("Please enter initiative:")
    if not tempInit:
        tempInit = 0

    tempDex = input("Please enter dex mod:")
    if not tempDex:
        tempDex = 0

    initiative_tracker.append(Character(tempChar, int(tempInit), int(tempDex)))
    print(f"You've added {tempChar} to the initiative order.")
    update_init_msg(True)


def update_init():
    tempChar = input(
        "Please enter the name of the character whose initiative you would like to change:"
    )
    match = False
    for entry in initiative_tracker:
        if entry.name == tempChar:
            match = True
            entry.initiative = int(input("Enter the new initiative value:"))
            entry.dexMod = int(input("Enter the new dex mod value:"))

    update_init_msg(match)


def del_char():
    tempChar = input("Please enter a character name:")
    match = False
    for ind, entry in enumerate(initiative_tracker):
        if entry.name == tempChar:
            match = True
            ans = input(f"Are you sure you want to delete: {entry.name}? (y/n, yes/no)")
            if ans == "y" or ans == "yes":
                del initiative_tracker[ind]

    update_init_msg(match)


def update_init_msg(match):
    if match == False:
        print("Failed to find a character with that name; check your spelling.")
    else:
        print("Updated the initiative order.")


def clear():
    print("\033c", end="", flush=True)


main()
