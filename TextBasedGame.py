# David A Garcia III

# import any module thats required for the text based game
import random
from sys import exit
from time import sleep
# Sets player inventory as list
player_inventory = []
# Sets player spawn point
player_room = "Prison Cell"
# Stores players name
user_name = ""
# This is the players map an locations for the game
player_map = {
        'Prison Cell': {"South": "Western Greathall"},

        'Western Greathall': {"North": "Prison Cell",
                              "East": "Central Greathall"},

        'Central Greathall': {"West": "Western Greathall",
                              "South": "Eastern Messhall",
                              "North": "Gaurd Barracks",
                              "East": "Eastern Greathall"},

        'Eastern Greathall': {"West": "Central Greathall",
                              "East": "Torture Chamber",
                              "North": "Library of Wizardry"},

        'Library of Wizardry': {"South": "Eastern Greathall"},

        'Torture Chamber': {"West": "Eastern Greathall",
                            "South": "Dragon Chamber"},

        'Dragon Chamber': {"North": "Torchure Chamber",
                           "East": "Grand Staircase"},

        'Grand Staircase': {"East": "Dragon Chamber"},

        'Gaurd Barracks': {"South": "Central Greathall",
                           "East": "Armory"},

        'Armory': {"West": "Gaurd Barracks"},

        'Eastern Messhall': {"North": "Central Greathall",
                             "South": "Bedrooms",
                             "West": "Western Messhall"},

        'Western Messhall': {"South": "Kitchen",
                             "East": "Eastern Messhall"},

        'Bedrooms': {"North": "Eastern Messhall"},

        'Kitchen': {"North": "Western Messhall"}
    }
# I only want certain events in the game to run once
# Once these values are set to True
barracks_has_run = False
eastern_hall_has_run = False
kitchen_has_run = False
bedrooms_has_run = False
wizard_library_has_run = False
dragon_chamber_has_run = False
torchure_chamber_has_run = False


# Reveals the player controls
def player_controls():
    print("\n")
    print('To move directions type "North", "South", "East" or "West"')
    print('To see inventory type "inventory"')
    print('To grab a item type "get [item name]"')
    print('To leave a item type "leave [item name]"')
    print('To quit the game type "exit"')
    print("\n")


# Shows the game rules
def rules():
    print("\n")
    print('You must aquire all items in order to win the game')
    print('You will only have one chance to aquire each item (6 items total)')
    print('If items are not collected you will die and lose the game')


# Player starts off in the main menu here
def main_menu():
    print("WELCOME TO DUNGEON WARRIOR")
    print("-"*26)

    while True:

        print("\nTo begin press 'S' to start game")
        print("To view controls press 'C'")
        print("To view rules press 'R'")
        print("To leave game press 'E'")

        user_input = input("\nEnter a valid command: ")

        if user_input.lower() == "s":

            backstory()
            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif user_input.lower() == "c":
            player_controls()

        elif user_input.lower() == "r":
            rules()

        elif user_input.lower() == "e":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("\n!!! Please enter a valid command !!!\n")


# Explains the story behind the game.
def backstory():
    global user_name

    print("In the early years of the kingdom the people flourished...")
    sleep(3)

    print("Over the years, the decades the kingdom\
 went through trials and tribulations...\n")
    sleep(3)

    print("During the hard times the peasants\
 learned to live with the hardships..")
    sleep(3)

    print("While the scum of the earth ruled in the castle\
 taking lives with meaningless war and bickering...\n")
    sleep(3)

    print("You were sworn to protect the kingdom.\
 Only for the corruption to reach your ranks..\n")
    sleep(3)

    print("You were drugged unconceious.")
    sleep(3)

    print("It is now your fate to find out why.")
    sleep(3)

    print("Escape the dark depths of the castles dungeon.")
    sleep(3)

    print("-" * 60)
    print("You awaken in a dark prison cell trying to remember who you are..")
    sleep(3)

    player_name = input("What is your name?: ")
    user_name = player_name

    print("-" * 60)


# This is where the game starts and takes in the run variables
def start(player_room, barracks_has_run,
          eastern_hall_has_run, bedrooms_has_run,
          kitchen_has_run, wizard_library_has_run,
          dragon_chamber_has_run, torchure_chamber_has_run):

    # Player enters a loop to traverse the map
    while True:
        print(f"{user_name}, you are currently in:", player_room)

        player_direction = input("Which way will you go?: ")
        print("-" * 60)

        if player_direction.title() in player_map[player_room]:
            player_room = player_map[player_room][player_direction.title()]

            # Checks if the player has executed the unique functions
            if player_room == "Gaurd Barracks" and barracks_has_run is False:
                barracks()

            elif (player_room == "Eastern Messhall" and
                  eastern_hall_has_run is False):
                eastern_messhall()

            elif player_room == "Bedrooms" and bedrooms_has_run is False:
                bedrooms()

            elif player_room == "Kitchen" and kitchen_has_run is False:
                kitchen()

            elif (player_room == "Library of Wizardry" and
                  wizard_library_has_run is False):
                wizard_library()

            elif (player_room == "Torture Chamber" and
                  torchure_chamber_has_run is False):
                torchure_chamber()

            elif (player_room == "Dragon Chamber" and
                  dragon_chamber_has_run is False):
                dragon_chamber()

        # Player has these options to check rules, inventory and controls
        # At any point in the game.
        elif player_direction.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_direction.lower() == "c":
            player_controls()

        elif player_direction.lower() == "r":
            rules()

        elif player_direction.lower() == "e":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("There's a wall in front of you. Try another way.\n")


# Special event for the player when they enter the barracks
def barracks():
    global barracks_has_run
    barracks_has_run = True

    print("You see a few gaurds standing in your way.")
    sleep(3)

    print("At a glance they look tough but exhausted..\
 They must've been on duty all day.\n")
    sleep(3)

    print("You need to take them out swiftly..\n")
    sleep(3)

    print('Should you A.) Sneak pass the gaurds to avoid them')
    sleep(3)

    print('Should you B.) Fist fight them (They dont look tough anyways.)\n')
    sleep(3)

    while True:

        player_decision = input("Choose your approach A/B: ")
        if player_decision.lower() == "a":
            player_sneak()

        elif player_decision.lower() == "b":
            player_attack()

        elif player_decision.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_decision.lower() == "c":
            player_controls()

        elif player_decision.lower() == "r":
            rules()

        elif player_decision.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")


def player_attack():
    print("The gaurds notice you soon as you walk up towards them.")
    sleep(3)

    print("They beat you mercilessly with no remorse only to get tired\n")
    sleep(3)

    print("You notice this and take advantage of the situation")
    sleep(3)

    print("You end up defeating the gaurds with your fist\
 barely escaping with your life\n")
    sleep(3)

    player_armor = input("You see your amror on the table\
 [get armor/leave armor]: ")

    if player_armor.lower() == "get armor":
        player_room = "Armory"
        player_inventory.append("Armor")

        print(f"You are now wearing the armor\
 you once used and went into the {player_room}\n")
        sleep(3)

        player_sword = input("You see a mounted sword that once belonged to\
 you what do you do? [get sword/leave sword]: ")

        if player_sword.lower() == "get sword":
            player_inventory.append("Sword")
            print("You are now weilding a trusty sword and armor\
 you must head back and find your way out...\n")

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_sword.lower() == "leave sword":
            print("You left your sword behind pondering\
 of the consequences ahead...")

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_sword.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_sword.lower() == "c":
            player_controls()

        elif player_sword.lower() == "r":
            rules()

        elif player_sword.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")

    if player_armor.lower() == "leave armor":
        player_room = "Armory"

        print("You left your armor behind thinking you made a mistake")
        print(f"You enter the {player_room} inspecting the\
 room you see a mounted sword.")

        player_sword = input("What do you do? [get sword/leave sword]: ")

        if player_sword.lower() == "get sword":
            player_inventory.append("Sword")

            print("You are now weilding a trusty sword without your\
 armor you must head back and find your way out...")

            start(player_room, barracks_has_run, eastern_hall_has_run,
                  bedrooms_has_run, kitchen_has_run,
                  wizard_library_has_run, dragon_chamber_has_run,
                  torchure_chamber_has_run)

        elif player_sword.lower() == "leave sword":
            print("You left your sword and armor behind\
 pondering of the consequences ahead...")

            start(player_room, barracks_has_run, eastern_hall_has_run,
                  bedrooms_has_run, kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_sword.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_sword.lower() == "c":
            player_controls()

        elif player_sword.lower() == "r":
            rules()

        elif player_sword.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")

    elif player_armor.lower() == "inventory":
        print("INVENTORY:", player_inventory)

    elif player_armor.lower() == "c":
        player_controls()

    elif player_armor.lower() == "r":
        rules()

    elif player_armor.lower() == "exit":
        exit("Thank you for playing Dungeon Warrior")

    else:
        print("Please enter a valid option")


def player_sneak():
    sneak = random.randint(1, 2)

    if sneak == 1:
        print("You have successfuly snuck passed the\
 gaurds and enterd the amrory..")

        player_room = "Armory"
        sleep(3)

        while True:
            player_sword = input("You see your trusty sword from years\
 of battles mounted what do you do?\
 [get sword/leave sword]: ")

            if player_sword.lower() == "get sword":
                player_inventory.append("Sword")
                print("You are now weilding your trusty sword")

                player_room = "Gaurd Barracks"
                print("With your sword in your hand you made easy work of\
 the exhuasted gaurds..")

                sleep(3)
                print("Apon inspecting the gaurds you find your trusty armor\
 on the table...")

                while True:
                    player_armor = input("You see your amror on the table\
 what do you do?\
 [get armor/leave armor]: ")

                    if player_armor.lower() == "get armor":
                        player_inventory.append("Armor")
                        print("You are now wearing your trust\
                               armor and weilding your sword...")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run,
                              bedrooms_has_run, kitchen_has_run,
                              wizard_library_has_run, dragon_chamber_has_run,
                              torchure_chamber_has_run)

                    elif player_armor.lower() == "leave armor":
                        print("You decided to leave your armor and\
 take your sword.\
 You wonder if you made a mistake...")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run,
                              bedrooms_has_run, kitchen_has_run,
                              wizard_library_has_run, dragon_chamber_has_run,
                              torchure_chamber_has_run)

                    elif player_armor.lower() == "inventory":
                        print("INVENTORY:", player_inventory)

                    elif player_armor.lower() == "c":
                        player_controls()

                    elif player_armor.lower() == "r":
                        rules()

                    elif player_armor.lower() == "exit":
                        exit("Thank you for playing Dungeon Warrior")

                    else:
                        print("Please enter a valid option")

            elif player_sword.lower() == "leave sword":
                player_room = "Gaurd Barracks"

                print("You left your sword behind without\
 thinking of the consequences")
                sleep(3)

                print("You go back into the gaurd barracks")
                sleep(3)

                print("The gaurds shocked that you were there beat you\
 mercilessly with no remorse only to get tired")
                sleep(3)

                print("You notice this and take advantage of the situation")
                sleep(3)

                print("You end up defeating the gaurds with your fist\
 barely escaping with your life")
                sleep(3)

                while True:
                    player_armor = input("You then see your armor on the \
 table what do you do?\
 [get armor/leave armor]: ")

                    if player_armor.lower() == "get armor":
                        player_inventory.append("Armor")

                        print("You are now wearing the armor\
 you once used but without\
 your sword")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run,
                              bedrooms_has_run, kitchen_has_run,
                              wizard_library_has_run, dragon_chamber_has_run,
                              torchure_chamber_has_run)

                    elif player_armor.lower() == "leave armor":
                        print("You have nothing to\
 defend your self with.\
 No armor. No Sword.\
 The consequences will be dire.")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run,
                              bedrooms_has_run, kitchen_has_run,
                              wizard_library_has_run, dragon_chamber_has_run,
                              torchure_chamber_has_run)

                    elif player_armor.lower() == "inventory":
                        print("INVENTORY:", player_inventory)

                    elif player_armor.lower() == "c":
                        player_controls()

                    elif player_armor.lower() == "r":
                        rules()

                    elif player_armor.lower() == "exit":
                        exit("Thank you for playing Dungeon Warrior")

                    else:
                        print("Please enter a valid option")

            elif player_sword.lower() == "inventory":
                print("INVENTORY:", player_inventory)

            elif player_sword.lower() == "c":
                player_controls()

            elif player_sword.lower() == "r":
                rules()

            elif player_sword.lower() == "exit":
                exit("Thank you for playing Dungeon Warrior")
            else:
                print("Please enter a valid option")

    elif sneak == 2:
        print("Oh no! the gaurds have found you. You must fight them!")
        sleep(3)

        print("The gaurds shocked that you were there beat\
 you mercilessly with no remorse only to get tired")
        sleep(3)

        print("You notice this and take advantage of the situation")
        sleep(3)

        print("You end up defeating the gaurds with your fist\
 barely escaping with your life")
        sleep(3)

        while True:
            player_armor = input("You see your armor on the\
 table what do you do?\
 [get armor/leave armor]: ")

            if player_armor.lower() == "get armor":
                player_inventory.append("Armor")
                player_room = "Armory"

                print(f"You are now wearing the armor you once\
 used and went into the {player_room}")
                sleep(3)

                while True:
                    player_sword = input("You see a mounted sword\
 that once belonged\
 to you what do you do?\
 [get sword/leave sword]: ")

                    if player_sword.lower() == "get sword":
                        player_inventory.append("Sword")

                        print("You are now weilding a trusty sword you must\
 head back and find your way out...")
                        sleep(2)

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run, bedrooms_has_run,
                              kitchen_has_run, wizard_library_has_run,
                              dragon_chamber_has_run, torchure_chamber_has_run)

                    elif player_sword.lower() == "leave sword":

                        print("You left your sword behind pondering\
 of the consequences ahead...")
                        sleep(2)

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run, bedrooms_has_run,
                              kitchen_has_run, wizard_library_has_run,
                              dragon_chamber_has_run, torchure_chamber_has_run)

                    elif player_sword.lower() == "inventory":
                        print("INVENTORY:", player_inventory)

                    elif player_sword.lower() == "c":
                        player_controls()

                    elif player_sword.lower() == "r":
                        rules()

                    elif player_sword.lower() == "exit":
                        exit("Thank you for playing Dungeon Warrior")

                    else:
                        print("Please enter a valid option")

            elif player_armor.lower() == "leave armor":
                player_room = "Armory"

                print(f"You left your armor wondering if the consequenses\
 will be dire as you head into the {player_room}.")

                while True:
                    player_sword = input("You see a mounted sword that once\
 belonged to you what do you do?\
 [get sword/leave sword]: ")

                    if player_sword.lower() == "get sword":
                        player_inventory.append("Sword")

                        print("You are now weilding a trusty sword\
 without your armor, you must head back\
 and find your way out...")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run, bedrooms_has_run,
                              kitchen_has_run, wizard_library_has_run,
                              dragon_chamber_has_run, torchure_chamber_has_run)

                    elif player_sword.lower() == "leave sword":
                        print("You left your sword and armor\
 behind pondering of the consequences ahead...")

                        start(player_room, barracks_has_run,
                              eastern_hall_has_run, bedrooms_has_run,
                              kitchen_has_run, wizard_library_has_run,
                              dragon_chamber_has_run, torchure_chamber_has_run)

                    elif player_sword.lower() == "inventory":
                        print("INVENTORY:", player_inventory)

                    elif player_sword.lower() == "c":
                        player_controls()

                    elif player_sword.lower() == "r":
                        rules()

                    elif player_sword.lower() == "exit":
                        exit("Thank you for playing Dungeon Warrior")

                    else:
                        print("Please enter a valid option")

            elif player_armor.lower() == "inventory":
                print("INVENTORY:", player_inventory)

            elif player_armor.lower() == "c":
                player_controls()

            elif player_armor.lower() == "r":
                rules()

            elif player_armor.lower() == "exit":
                exit("Thank you for playing Dungeon Warrior")

            else:
                print("Please enter a valid option")


def eastern_messhall():
    global eastern_hall_has_run
    eastern_hall_has_run = True

    print("You walk in and see an empty mess hall.")
    sleep(3)

    print("You wonder where everyone is at\n")
    sleep(3)

    print("You see your shield mounted as a trophy")
    sleep(3)

    print("You wonder why they are doing so\n")
    sleep(3)

    player_room = "Eastern Messhall"

    while True:
        player_shield = input("You look at the what should you do?\
 [get shield/leave shield]: ")
        print("\n")

        if player_shield.lower() == "get shield":
            player_inventory.append("Shield")

            print("You have aquired your shield..")
            sleep(3)

            print("You must look for the rest of your items to escape..\n")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_shield.lower() == "leave shield":
            print("You decided to not take your shield..")
            sleep(3)

            print("You decide to keep going.. was that a mistake?\n")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_shield.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_shield.lower() == "c":
            player_controls()

        elif player_shield.lower() == "r":
            rules()

        elif player_shield.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")


def bedrooms():
    global bedrooms_has_run
    bedrooms_has_run = True

    player_room = "Bedrooms"

    print(f"You enter the {player_room}.\
 You only see dying sick woman and children.")
    sleep(3)

    print("You wonder where the men have gone\n")
    sleep(3)

    print("You go looking around and you see your\
 helmet being worn by a corpse")
    sleep(3)

    print("You wonder why the had your helmet..\n")
    sleep(3)

    while True:
        player_shield = input("You look at the helmet what\
 should you do?\
 [get helmet/leave helmet]: ")

        if player_shield.lower() == "get helmet":
            player_inventory.append("Helmet")

            print("You have aquired your helmet..\
 It smells foul but nothing you cant handle")
            sleep(3)

            print("You must look for the rest of your items to escape..")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_shield.lower() == "leave helmet":
            print("You decided to not take your helmet..\
 its abosolutely disgusting")
            sleep(3)

            print("You decide to keep going.. will you need the helmet?\n")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_shield.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_shield.lower() == "c":
            player_controls()

        elif player_shield.lower() == "r":
            rules()

        elif player_shield.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")


def kitchen():
    global kitchen_has_run
    kitchen_has_run = True

    print("You arrive at the kitchen.")
    sleep(3)

    print("You notice human flesh has been been chopped\
 into pieces for the peasants\n")
    sleep(3)

    print("You now know why the people are starving and\
 the woman and children are starving")
    sleep(3)

    print("They refuse to eat their loved ones...\n")
    sleep(3)

    player_room = "Kitchen"

    while True:
        stamina_potion = input("You look around and see\
 a stamina potion what do\
 you do?\
 [get stamina potion/\
 leave stamina potion]: ")

        if stamina_potion.lower() == "get stamina potion":
            player_inventory.append("Stamina Potion")

            print("You have aquired your stamina potion..")
            sleep(3)

            print("An angry cook blindsides you from the\
 left, ready to chop you up for meat..")
            sleep(3)

            if "Sword" in player_inventory:
                print("You Pull out your sword from your shieth")
                sleep(3)

                print("You see his bloodlust in his eyes")
                sleep(3)

                print("You managed to dodge his tackle and\
 swiped his throat with your sword")
                sleep(3)

                print("You collect yourself and push forward\
 knowing you must free everyone...")
                sleep(3)

                start(player_room, barracks_has_run,
                      eastern_hall_has_run, bedrooms_has_run,
                      kitchen_has_run, wizard_library_has_run,
                      dragon_chamber_has_run, torchure_chamber_has_run)

            else:
                print("You ball your first ready to take him out..")
                sleep(3)

                print("You see his bloodlust in his eyes")
                sleep(3)

                print("You start punching him as he is slow on his feet..")
                sleep(3)

                print("After struggling you manage to get\
 behind him and break his neck with anger...")
                sleep(3)

                print("You collect yourself and push forward\
 knowing you must free everyone...")
                sleep(3)

                start(player_room, barracks_has_run,
                      eastern_hall_has_run, bedrooms_has_run,
                      kitchen_has_run, wizard_library_has_run,
                      dragon_chamber_has_run, torchure_chamber_has_run)

        elif stamina_potion.lower() == "leave stamina potion":
            print("You leave the potion behind only for you to\
 hear footsteps come from your left..\n")
            sleep(3)

            print("An angry cook blindsides you, ready\
 to chop you up for meat..\n")
            sleep(3)

            if "Sword" in player_inventory:
                print("You Pull out your sword from your shieth")
                sleep(3)

                print("You see his bloodlust in his eyes\n")
                sleep(3)

                print("You managed to dodge his tackle and swiped his\
 throat with your sword")
                sleep(3)

                print("You collect yourself and push forward\
 knowing you must free everyone...\n")
                sleep(3)

                start(player_room, barracks_has_run,
                      eastern_hall_has_run, bedrooms_has_run,
                      kitchen_has_run, wizard_library_has_run,
                      dragon_chamber_has_run, torchure_chamber_has_run)

            else:
                print("You ball your first ready to take him out..")
                sleep(3)

                print("You see his bloodlust in his eyes\n")
                sleep(3)

                print("You start punching him as he is slow on his feet..")
                sleep(3)

                print("After struggling you manage to get behind him and\
 break his neck with anger...\n")
                sleep(3)

                print("You collect yourself and push forward knowing\
 you must free everyone...")
                sleep(3)

                start(player_room, barracks_has_run,
                      eastern_hall_has_run, bedrooms_has_run,
                      kitchen_has_run, wizard_library_has_run,
                      dragon_chamber_has_run, torchure_chamber_has_run)

        elif stamina_potion.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif stamina_potion.lower() == "c":
            player_controls()

        elif stamina_potion.lower() == "r":
            rules()

        elif stamina_potion.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")


def wizard_library():
    global wizard_library_has_run
    wizard_library_has_run = True

    print("You see the demonic wizard library.")
    sleep(3)

    print("You wonder if anything will be useful in there")
    sleep(3)

    print("You open the door and see the hell priest dead on the table")
    sleep(3)

    print('You noticed he sacraficed him self on "purpose"')
    sleep(3)

    player_room = "Library of Wizardry"

    while True:
        player_potion = input("You see a magic potion lodged in the hell\
 priest skull what do you do?\
 [get magic potion/leave magic potion]: ")

        if player_potion.lower() == "get magic potion":
            player_inventory.append("Magic Potion")

            print("You have aquired the magic potion..")
            sleep(3)

            print("You must look for the rest of your items to escape..")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_potion.lower() == "leave magic potion":
            print("You decided to leave the potion where it sits..")
            sleep(3)

            print("You decide to keep going..how will you escape?")
            sleep(3)

            start(player_room, barracks_has_run,
                  eastern_hall_has_run, bedrooms_has_run,
                  kitchen_has_run, wizard_library_has_run,
                  dragon_chamber_has_run, torchure_chamber_has_run)

        elif player_potion.lower() == "inventory":
            print("INVENTORY:", player_inventory)

        elif player_potion.lower() == "c":
            player_controls()

        elif player_potion.lower() == "r":
            rules()

        elif player_potion.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("Please enter a valid option")


def torchure_chamber():
    global torchure_chamber_has_run
    torchure_chamber_has_run = True

    print("You have reached the torchure chamber")
    sleep(3)

    print("You are afraid of what you might find in there")
    sleep(3)

    print("You walk in. It smells of rotting flesh..")
    sleep(3)

    print('You see haning bodies of many differnt people')
    sleep(3)

    print("You think to your self how can the King\
 and superiors stoop this low")
    sleep(3)

    print("You see a massive iron gate..")
    sleep(3)

    print("You know what lurks behind..a..Dragon")
    sleep(3)

    print("If you push forward without all your gear you will be doomed..")
    sleep(3)

    player_room = "Torture Chamber"
    start(player_room, barracks_has_run,
          eastern_hall_has_run, bedrooms_has_run,
          kitchen_has_run, wizard_library_has_run,
          dragon_chamber_has_run, torchure_chamber_has_run)


def dragon_chamber():
    global dragon_chamber_has_run
    dragon_chamber_has_run = True

    print("You managed to open the iron gate")
    sleep(3)

    print("You see a dragon roaming free..")
    sleep(3)

    print("It immedately charges at you")
    sleep(3)

    if len(player_inventory) == 6:
        print("You dodge the attack")
        sleep(3)

        print("You ready your sword and shield\n")
        sleep(3)

        print("the dragon sprays blue fire from his mouth")
        sleep(3)

        print("You cover your body from the fire with your shield...\n")
        sleep(3)

        print("Amazed by the power of the dragon. \
 You see it fly up and goes for your head")
        sleep(3)

        print("Your helmet protected you from the air attack\n")
        sleep(3)

        print("You roll over, you notice you are getting exhuasted,\
 you drink the stamina potion")
        sleep(3)

        print("With more energy. You pop your magic potion and cast\
 a massive fire ball\n")
        sleep(3)

        print("The dragon has no chance...")
        sleep(3)

        print("As you charge your fire ball to the maximum potential.\
 The dragon charges you head on...\n")
        sleep(3)

        print("Once the dragon was in your face you release the fire\
 ball leaving a massive explosion.")
        sleep(3)

        print("In the smoke you are on your knees. Weakend by the explosion.\
 you wonder off to the grand staricase\
 to freedom..to enact your revenge..\n")
        sleep(3)
        exit(f"{user_name}, congradulations you escaped the\
 castle dungeon...To be continued...")

    elif len(player_inventory) < 6:
        print("While quick on your feet.\
 You managed to dodge the inital attack")
        sleep(3)

        print("Without all your gear you could not take the dragon.")
        sleep(3)

        print("With one swift attack the dragon took your head in seconds..")
        exit(f"{user_name}, you lose.. the dragon was too powerful...")


# Make sure file does not run when imported
if __name__ == "__main__":
    main_menu()
