def main():
    inventory = []
    found_note = False
    found_key = False
    found_screwdriver = False
    in_room = True
    escaped = False
    dead = False

    print("find the elder wand and escape the building.")
    print("\nwhat do you do?")

    while in_room:
        print("1. look around the room")
        print("2. check under the bed")
        print("3. see whats in the closet")
        print("4. inspect the desk drawer")
        print("5. try the door")
        print("6. examine an air vent")
        choice = input("choose what to do: \n")

        if choice == "1":
            print("you are in a small room. the room contains a bed, a closet, a small desk with one drawer, and an air vent. the door is closed. the furniture looks old and the room isnt decorated.")
        elif choice == "2": 
            print("nothing else but dust bunnies.") if found_note == True else print("you find a crumpled piece of paper that reads 'red is sus'. below the text, there is a photo of a red among us character venting."), inventory.append("note"), 
            found_note = True
        elif choice == "3":
            print("stop checking in here silly.") if found_screwdriver == True else print("you step on something sharp, its a screwdriver."), inventory.append("screwdriver"), 
            found_screwdriver = True
        elif choice == "4":
            print("youve already looked here.") if found_key == True else print("you find a shiny gold key."), inventory.append("key"), 
            found_key = True
        elif choice == "5":
            in_room = True,
            print("you unlock the door and step out into a dimly lit hallway. it continues to the left and right, with a doorway set opposite you.") if found_key == True else print("the door is locked, no you cant punch it."), inventory.pop("key")
        elif choice == "6":
            dead = True,
            print("you unscrew the vent cover and crawl in. you fall into a room full of death eaters and they kill you. better luck next time.") if found_screwdriver == True else print("there is a cover on the grate, held in by tiny screws."), inventory.pop("key")
        else:
            print("there are 6 options, this is not one of them")
        
if __name__ == "__main__":
    main()