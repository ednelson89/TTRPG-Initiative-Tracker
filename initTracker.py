import sys
import json
import os


class Character:
    def __init__(self, name, initiative, dexMod, manualSet):
        self.name = name
        self.initiative = initiative
        self.dexMod = dexMod
        self.manualSet = manualSet


initiative_tracker = []
test_mode = False

# For test/demo purposes, allow a command line arg to populate the order
if len(sys.argv) == 2 and sys.argv[1] == "test":
    test_mode = True
    initiative_tracker.append(Character("Starost", 20, 0, 0))
    initiative_tracker.append(Character("Lisp", 18, 1, 0))
    initiative_tracker.append(Character("Trapspringer", 18, 2, 0))
    initiative_tracker.append(Character("Eirikr", 5, 1, 0))
    initiative_tracker.append(Character("Kalevin", 5, 1, 1))
    initiative_tracker.append(Character("Llewyn", 10, 0, 2))


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
            case "5":  # 5 Import a party file
                clear()
                import_party()
                input()
            case "6":  # 6 Export party file
                clear()
                export_party()
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
    initiative_tracker.sort(key=lambda x: x.manualSet, reverse=False)
    initiative_tracker.sort(key=lambda x: x.dexMod, reverse=True)
    initiative_tracker.sort(key=lambda x: x.initiative, reverse=True)


def instruction_query():
    print("Would you like to :")
    print("1. Display Current Order")
    print("2. Add a Character")
    print("3. Change a character's initiative")
    print("4. Remove a character from the initiative order")
    print("5. Import a party from a .json file")
    print("6. Export a party to a .json file")
    print("0. EXIT")

    in_number = input("Please enter the number of the option you'd like: ")
    return in_number


def add_char():
    tempChar = input("Please enter a character name (required): ")
    if not tempChar:
        print("Character name required. Returning to menu.")
        return

    tempInit = int(input("Please enter initiative: ") or 0)
    tempDex = int(input("Please enter dex mod: ") or 0)
    tempSet = int(
        input(
            "If multiple characters have the same initiative and dex mod,\n manually set where in the order they go. Lower numbers go first.\n Otherwise, just hit enter:"
        )
        or 0
    )

    initiative_tracker.append(
        Character(tempChar, int(tempInit), int(tempDex), int(tempSet))
    )
    print(f"You've added {tempChar} to the initiative order.")
    update_init_msg(True)


def update_init():
    print(
        "Please enter the name of the character whose initiative you would like to change: "
    )
    print(get_name_list())
    tempChar = input()

    match = False
    for entry in initiative_tracker:
        if entry.name == tempChar:
            match = True
            entry.initiative = int(
                input(
                    "Enter the new initiative value (providing no value will set to 0): "
                )
                or 0
            )
            entry.dexMod = int(
                input(
                    "Enter the new dex mod value (providing no value will set to 0): "
                )
                or 0
            )
            entry.manualSet = int(
                input(
                    "Enter the new manual set value (providing no value will set to 0): "
                )
                or 0
            )

    update_init_msg(match)


def del_char():
    print("Please enter a character name: ")
    print(get_name_list())
    tempChar = input()

    match = False
    for ind, entry in enumerate(initiative_tracker):
        if entry.name == tempChar:
            match = True
            ans = input(
                f"Are you sure you want to delete: {entry.name}? (y/n, yes/no) "
            )
            if ans == "y" or ans == "yes":
                del initiative_tracker[ind]

    update_init_msg(match)


def update_init_msg(match):
    if match == False:
        print("Failed to find a character with that name; check your spelling.")
    else:
        print("Updated the initiative order.")


def get_name_list():
    tempList = ""
    for entry in initiative_tracker:
        tempList += entry.name + ", "
    return tempList[:-2]


def import_party():
    tempName = get_party_name()
    tempText = load_party_file(tempName)

    for entry in tempText:
        initiative_tracker.append(
            Character(
                entry["name"],
                int(entry["initiative"]),
                int(entry["dexMod"]),
                int(entry["manualSet"]),
            )
        )
    clear()
    print("File Imported")
    list_order()


def get_party_name():
    # Get a list of Save Files for Ease of Use
    filePath = "./PartyLists/"
    filesList = []
    files = os.listdir(filePath)
    for file in files:
        temp = file.removesuffix(".json")
        filesList.append(temp)

    # Output the list so that users can reference the options
    print("Party/Encounter Names:")
    print(*filesList, sep=", ")
    return input(
        "Please input the name of the party you wish to load (ex. Wanderers): "
    )


def load_party_file(partyName):
    temp_Path = f"PartyLists/{partyName}.json"
    try:
        f = open(temp_Path)
        return json.load(f)
    except:
        print("Oops, the party name does not exist, please try again.")
        return ""


def export_party():
    party_name = input(
        "Please input the name you wish to save this party as (ex. 6kobolds): "
    )
    temp_data = json.dumps(initiative_tracker, default=lambda x: x.__dict__)
    with open(f"PartyLists/{party_name}.json", "w") as outfile:
        outfile.write(temp_data)
    clear()
    print(
        f"Export Complete. You can find your save file for the party name {party_name} in the PartyLists subdirectory."
    )


def clear():
    print("\033c", end="", flush=True)


main()
