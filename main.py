import sys


class Character:
    def __init__(self, name, initiative, dexMod):
        self.name = name
        self.initiative = initiative
        self.dexMod = dexMod


initiative_tracker = []

initiative_tracker.append(Character("test1", 20, 0))
initiative_tracker.append(Character("test2", 18, 1))
initiative_tracker.append(Character("test3", 18, 2))


def main():
    print("***Welcome to the Initiaive Tracker***")

    run = True
    while run == True:
        command = instruction_query()

        match command:
            case "1":  # 1 Display current order
                list_order()
                input()
            case "2":  # 2 Add a Character
                add_char()
                input()
            case "3":  # 3 Change a characters initiative
                update_init()
                input()
            case "0":
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
    print("0. EXIT")

    print("Please enter the number of the option you'd like:")
    in_number = input()
    return in_number


def add_char():
    print("Please enter a character name:")
    tempChar = input()
    print("Please enter initiative:")
    tempInit = input()
    print("Please enter dex mod:")
    tempDex = input()

    initiative_tracker.append(Character(tempChar, int(tempInit), int(tempDex)))
    print(f"You've added {tempChar} to the initiative order.")


def update_init():
    print(
        "Please enter the name of the character whose initiative you would like to change:"
    )
    tempChar = input()
    match = False
    for entry in initiative_tracker:
        if entry.name == tempChar:
            match = True
            print("Enter the new initiative value:")
            entry.initiative = int(input())
            print("Enter the new dex mod value:")
            entry.dexMod = int(input())
    if match == False:
        print("Failed to find a character with that name; check your spelling.")
    else:
        print("Updated initiative.")


def clear():
    print("\033c", end="", flush=True)


main()
