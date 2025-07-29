def main():
    inventory = set()
    found_note = False
    found_key = False
    found_screwdriver = False
    escaped = False

    print("you wake up in a room. the door is closed\n")

    while not escaped:
        print("\nwhat do you do?")
        print("1. look around the room")
        print("2. check under the bed")
        print("3. see whats in the closet")
        print("4. inspect the desk drawer")
        print("5. try the door")
        print("6. examine an air vent")
        choice = input("choose what to do: ")

        if choice == "1":
            print("you are in a small room. the room contains a bed, a closet, a small desk with one drawer, and an air vent. the furniture looks old and the room isnt decorated.")
        elif choice == "2":
        elif choice == "3":
        elif choice == "4":
        elif choice == "5":
        else choice == "6":

if __name__ == "__main__":
    main()