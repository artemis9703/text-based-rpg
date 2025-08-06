def main():
    #start room items
    found_note = False
    found_key = False
    found_screwdriver = False

    #opposite hallway puzzle items
    found_square = False
    found_triangle = False
    found_star = False
    found_circle = False
    blocks_complete = False
    
    # left door
    found_crackers = False

    #fireplace
    found_coin = False

    #closet
    found_dog = False

    #password
    found_crystal = False

    #locations
    room = True
    hallway = False
    left = False
    opposite = False
    pw = False
    fireplace = False
    closet = False
    exit = False
    escaped = False
    dead = False

    print("if you want to pick option 1. or 2. and so on, then enter 1 or 2 and so on as your answer.\nyou are a find the ancient power stone and escape the building.")

    while True:
        if room:
            print("\nwhat do you do?")
            print("\n1. look around the room")
            print("2. check under the bed")
            print("3. see whats in the closet")
            print("4. inspect the desk drawer")
            print("5. try the door")
            print("6. examine an air vent")
            print("7. freak out")
            choice = input("choose what to do: \n")

            if choice == "1":
                print("you are in a small room. the room contains a bed, a closet, a small desk with one drawer, and an air vent. the door is closed. the furniture looks old and the room isnt decorated.")
            elif choice == "2": 
                print("nothing else but dust bunnies.") if found_note == True else print("you find a crumpled piece of paper that reads 'red is sus'. below the text, there is a photo of a red among us character venting.")
                found_note = True
            elif choice == "3":
                print("stop checking in here silly.") if found_screwdriver == True else print("you step on something sharp, its a screwdriver.")
                found_screwdriver = True
            elif choice == "4":
                print("youve already looked here.") if found_key == True else print("you find a shiny gold key.")
                found_key = True
            elif choice == "5":
                if found_key == True:
                    print("you unlock the door and step out into a dimly lit hallway. it continues to doors on the left and right, with another doorway set opposite you.")
                    room = False
                    hallway = True
                else:
                    print("the door is locked, no you cant punch it.")
            elif choice == "6":
                if found_screwdriver == True:
                    print("you unscrew the vent cover and crawl in. you fall into a room full of enemy wizards and they kill you. better luck next time.")
                    dead = True
                    room = False
                else:
                    print("there is a cover on the grate, held in by tiny screws.")
            elif choice == "7":
                print("you freaked out.")
                dead = True
                room = False
            else:
                print("guys there are 7 options, this is not one of them.")

        elif hallway:
            print("\nwhat do you do?")
            print("\n1. head down the hallway to the left door")
            print("2. head down the hallway to the right door")
            print("3. try the door opposite you")
            print("4. go back into the room")
            choice = input("choose what to do: \n")

            if choice == "1":
                hallway = False
                left = True
                print("you walk down the hallway and open the door.")
            elif choice == "2":
                hallway = False
                dead = True
                print("you walk down the hallway and open the door. a stream of green light hits you in the chest and you die.")
            elif choice == "3":
                hallway = False
                opposite = True
                print("you cross the hallway and slowly push the door open.")
            elif choice == "4":
                hallway = False
                room = True
                print("coward.")
            else:
                print("guys there are 4 options, this is not one of them.")     

        elif left:
            print("\nwhat do you do?")
            print("\n1. look around the room")
            print("2. look in the wardrobe")
            print("3. check in the desk")
            print("4. look under the bed")
            choice = input("choose what to do: \n")

            if choice == "1":
                print("you look around and notice a few things. there is an old bed and matching desk, an old looking wardrobe sits against the right wall. the whole room isnt decorated and has a musty smell.")
            elif choice == "2":   
                print("you open the large wardrobe and step inside, the door closes behind you.")
                left = False
                closet = True
            elif choice == "3":
                print("seriously, stop looking in places youve already checked.") if found_crackers == True else print("you find a package of crackers that looks new.")
                found_crackers = True
            elif choice == "4":
                print("you get a spiderweb on your face, but nothing else.")
            else:
                print("guys there are 4 options, this is not one of them.")                                             

        elif opposite:
            print("\nwhat do you do?")
            print("\n1. look around the room") #found_square = False found_triangle = False found_star = False found_circle = False
            print("2. check in the desk")
            print("3. move the painting")
            print("4. examine the side table")
            print("5. crawl under the bed")
            print("6. open the closet")
            choice = input("choose what to do: \n")

            if choice == "1":
                print("you see a desk, closet door, a bed, and a side table. this room is more decorated than the others, with elaborate paintings hanging on the walls.")
            elif choice == "2":   
                if found_square == True:
                    print("just as before, there is nothing in or on the desk.")
                else:
                    found_square = True
                    print("you walk to the desk and open the drawer. nothing that you can see but as you shake the desk a bit, a small wooden square falls from the lamp shade.")
            elif choice == "3":
                if found_triangle == True:

                else:

            elif choice == "4":
                if found_square == True & found_triangle == True & found_star == True & found_circle == True:

                else:

            elif choice == "5":
                if found_star == True:

                else:

            elif choice == "6":
                if found_circle == True:
                    
                else:
            
            else:
                print("guys there are 6 options, this is not one of them.")

        elif pw:
            print("\nwhat do you do?")
            print("\n")
            print("")
            print("")
            choice = input("choose what to do: \n")

            if choice == "1":

            elif choice == "2":   

            elif choice == "3":

            else:
                print("guys there are 3 options, this is not one of them.")

        elif fireplace:
            print("\nwhat do you do?")
            print("\n")
            print("")
            print("")
            choice = input("choose what to do: \n")

            if choice == "1":

            elif choice == "2":   

            elif choice == "3":

            else:
                print("guys there are 3 options, this is not one of them.")

        elif closet:
            print("\nwhat do you do?")
            print("\n1. look around the inside of the wardrobe")
            print("2. pull the left lever")
            print("3. pull the right lever")
            print("4. try to get out of the wardrobe")
            choice = input("choose what to do: \n")

            if choice == "1":
                print("as you glance around the inside, a small torch flickers to life on the wall opposite you. you see a rusty metel lever to your left and another to your right. you see a slot for a circluar item with a star indent to be pressed into on the opposite wall, a clear casing covers it.")
            elif choice == "2":   
                if found_coin == True:
                    exit = True
                    closet = False
                    print("you tug the left lever toward you. you hear a loud click and a panel in the wall slids open. the clear casing on the circular indent slids away. you realize it is the same symbol on the strange coin you found. you push the coin into the slot and hear a loud click. the opposite wall slides away")
                else:    
                    print("you tug the left lever toward you. you hear a loud click and a panel in the wall slids open. the clear casing on the circular indent slids away.")
            elif choice == "3":
                if found_crackers == True:
                    found_dog = True
                    print("a panel in the wall slids open and an angry dog steps through, snarling. you remember the crackers in your pocket and give some to the dog. the dog is now your friend.")
                else:
                    closet = False
                    dead = True
                    print("a panel in the wall slids open and an angry dog steps through, snarling. the dog kills you.")
            elif choice == "4":
                closet = False
                left = True
                print("you throw your shoulder against the door and it flies open.")

            else:
                print("guys there are 4 options, this is not one of them.")

        elif exit:
            print("\nwhat do you do?")
            print("\n1. ")

        elif dead:
            print("\nwhat do you do?")
            print("\n1. restart")
            print("2. give up and live with your failure")
            choice = input("choose what to do: \n")

            if choice == "1":
                found_note = False
                found_key = False
                found_screwdriver = False
                found_square = False
                found_triangle = False
                found_star = False
                found_circle = False
                blocks_complete = False
                found_crackers = False
                found_coin = False
                found_dog = False
                found_crystal = False
                room = True
                dead = False
                print("valiant choice, young wizard")
            elif choice == "2":
                print("congrats, you failed. close this tab and throw your device at the nearest wall.")
                exit()
            else:
                print("guys there are 2 options, this is not one of them")

        elif escaped:
            print("thank you, you will go down in history as a great wizard.")                

if __name__ == "__main__":
    main()