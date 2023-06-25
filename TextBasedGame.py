# David A Garcia III

# import any module thats required for the text based game 
import random
import pygame
from sys import exit
from time import sleep

player_inventory = []
player_room = "Prison Cell"
objective = "Retrieve your items and escape"

player_map = {
        'Prison Cell':{"South": "Western Greathall"},

        'Western Greathall': {"North":"Prison Cell", "East": "Central Greathall"},
        'Central Greathall': {"West":"Western Greathall", "South":"Eastern Messhall", "North":"Gaurd Barracks", "East":"Eastern Greathall"},
        'Eastern Greathall': {"West":"Central Greathall", "East":"Torture Chamber", "North":"Library of Wizardry"},

        'Library of Wizardry':{"South":"Eastern Greathall"},

        'Torture Chamber':{"West":"Eastern Greathall", "South":"Dragon Chamber"},
        'Dragon Chamber':{"North":"Torchure Chamber","West":"Grand Staircase"},

        'Gaurd Barracks': {"South":"Central Greathall", "East":"Armory"},
        'Armory':{"West":"Gaurd Barracks"},

        'Eastern Messhall':{"North":"Central Greathall", "South":"Bedrooms", "West": "Western Messhall"},
        'Western Messhall':{"South":"Kitchen","East":"Eastern Messhall"},

        'Bedrooms':{"North":"Eastern Messhall"},
        'Kitchen':{"North":"Western Messhall"}


    }

barracks_has_run = False
eastern_hall_has_run = False
kitchen_has_run = False
bedrooms_has_run = False
wizard_library_has_run = False

def player_controls():
        print("\n")
        print('To move directions type "North", "South", "East" or "West"')
        print('To see inventory type "inventory"')
        print('To grab a item type "get [item name]"')
        print('To leave a item type "leave [item name]"')
        print('To quit the game type "exit"')

def main_menu():
    print("WELCOME TO DUNGEON WARRIOR")
    print("-"*26)
    while True:
        print("\nTo begin press 'S' to start game")
        print("To view controls press 'C'")
        user_input = input("\nEnter a valid command: ")
        if user_input.lower() == "s":
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif user_input.lower() == "c":
            player_controls()
        elif user_input.lower() == "exit":
             exit("Thank you for playing Dungeon Warrior")
        else:
             print("\n!!! Please enter a valid command !!!\n")

def backstory():
    print("In the early years of the kingdom the people flourished...")
    sleep(3)
    print("Over the years, the decades the kingdom went through trials and tribulations...")
    sleep(4)
    print("During the hard times the peasants learned to live with the hardships..")
    sleep(4)
    print("While the scum of the earth ruled in the castle taking lives with meaningless war and bickering...")
    sleep(4)
    print("You were sworn to protect the kingdom. Only for the corruption to reach your ranks..")
    sleep(4)
    print("You were drugged unconceious.")
    sleep(3)
    print("It is now your fate to find out why.")
    sleep(3)
    print("Escape the dark depths of the castles dungeon.")
    sleep(3)
    print("-" * 60)
    print("You awaken in a dark cell trying to remember who you are..")
    sleep(3)
    player_name = input("What is your name?: ")
    print("-" * 60)

def start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run):
    while True:
        #print(f"{player_name}, you are currently in:", player_room)
        print("you are currently in:", player_room)
        player_direction = input("Which way will you go?: ")
        print("\n")

        if player_direction.title() in player_map[player_room]:
            player_room = player_map[player_room][player_direction.title()]

            if player_room == "Gaurd Barracks" and barracks_has_run == False:
                barracks()
                barracks_has_run = True

            elif player_room == "Eastern Messhall" and eastern_hall_has_run == False:
                eastern_messhall()
                eastern_hall_has_run = True

            elif player_room == "Bedrooms" and bedrooms_has_run == False:
                bedrooms()
                bedrooms_has_run = True

            elif player_room == "Kitchen" and kitchen_has_run == False:
                kitchen()
                kitchen_has_run = True

            elif player_room == "Wizard's Library" and wizard_library_has_run == False:
                wizard_library()
                wizard_library_has_run = True

        elif player_direction.lower() == "c":
            player_controls()
        elif player_direction.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("There's a wall in front of you. Try another way.\n")

def barracks():
    print("You see a few gaurds standing in your way.")
    sleep(3)
    print("At a glance they look tough but exhausted..They must've been on duty all day.")
    sleep(3)
    print("You need to take them out swiftly..")
    sleep(3)
    print('Should you A.) Sneak pass the gaurds to avoid them')
    sleep(3)
    print('Should you B.) Fist fight them (They dont look tough anyways)')
    sleep(3)

    while True:
        player_decision = input("Choose your approach A/B: ")
        if player_decision.lower() == "a":
            player_sneak()
        elif player_decision.lower() == "b":
            player_attack()
        else:
            print("Please enter a valid option")

def player_attack():
    print("The gaurds notice you soon as you walk up towards them.")
    sleep(3)
    print("They beat you mercilessly with no remorse only to get tired")
    sleep(3)
    print("You notice this and take advantage of the situation")
    sleep(3)
    print("You end up defeating the gaurds with your fist barely escaping with your life")
    sleep(3)

    player_armor = input("You see your amror on the table [get armor/leave armor]: ")

    if player_armor.lower() == "get armor":
        player_room = "Armory"
        player_inventory.append("Armor")
        print(f"You are now wearing the armor you once used and went into the {player_room}")
        sleep(3)
        player_sword = input("You see a mounted sword that once belonged to you what do you do? [get sword/leave sword]: ")

        if player_sword.lower() == "get sword":
            player_inventory.append("Sword")
            print("You are now weilding a trusty sword and armor you must head back and find your way out...")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)

        elif player_sword.lower() == "leave sword":
            print("You left your sword behind pondering of the consequences ahead...")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")

    if player_armor.lower() == "leave armor":
        player_room = "Armory"
        print("You left your armor behind thinking you made a mistake")
        print(f"You enter the {player_room} inspecting the room you see a mounted sword.")
        player_sword = input("What do you do? [get sword/leave sword]: ")

        if player_sword.lower() == "get sword":
            player_inventory.append("Sword")
            print("You are now weilding a trusty sword without your armor you must head back and find your way out...")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif player_sword.lower() == "leave sword":
            print("You left your sword and armor behind pondering of the consequences ahead...")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")

def player_sneak():
    barracks_has_run = True
    sneak = random.randint(1,3)
    if sneak == 1:
        print("You have successfuly snuck passed the gaurds and enterd the amrory..")
        player_room = "Armory"
        sleep(3)
        while True:
            player_sword = input("You see your trusty sword from years of battles mounted what do you do? [get sword/leave sword]: ")
            if player_sword.lower() == "get sword":
                player_inventory.append("Sword")
                print("You are now weilding your trusty sword")

                if barracks_has_run == True:
                    player_room = "Gaurd Barracks"
                    print("With your sword in your hand you made easy work of the exhuasted gaurds..")
                    sleep(1)
                    print("Apon inspecting the gaurds you find your trusty armor on the table...")

                    player_armor = input("You see your amror on the table what do you do? [get armor/leave armor]: ")
                    if player_armor.lower() == "get armor":
                        player_inventory.append("Armor")
                        print("You are now wearing your trust armor and weilding your sword...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
                    elif player_armor.lower() == "leave armor":
                        print("You decided to leave your armor and take your sword. You wonder if you made a mistake...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
                    else:
                        print("Please enter a valid option")
            elif player_sword.lower() == "leave sword":
                player_room = "Gaurd Barracks"
                print("You left your sword behind without thinking of the consequences")
                sleep(3)
                print("You go back into the gaurd barracks")
                sleep(3)
                print("The gaurds shocked that you were there beat you mercilessly with no remorse only to get tired")
                sleep(3)
                print("You notice this and take advantage of the situation")
                sleep(3)
                print("You end up defeating the gaurds with your fist barely escaping with your life")
                sleep(3)
                while True:
                    player_armor = input("You then see your armor on the table what do you do? [get armor/leave armor]: ")
                    if player_armor.lower() == "get armor":
                        player_inventory.append("Armor")
                        print("You are now wearing the armor you once used but without your sword")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
                    elif player_armor.lower() == "leave armor":
                        print("You have nothing to defend your self with. No armor. No Sword. The consequences will be dire.")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
            else:
                print("Please enter a valid option")
    elif sneak == 2:
        print("Oh no! the gaurds have found you. You must fight them!")
        sleep(3)
        print("The gaurds shocked that you were there beat you mercilessly with no remorse only to get tired")
        sleep(3)
        print("You notice this and take advantage of the situation")
        sleep(3)
        print("You end up defeating the gaurds with your fist barely escaping with your life")
        sleep(3)
        while True:
            player_armor = input("You see your armor on the table what do you do? [get armor/leave armor]: ")

            if player_armor.lower() == "get armor":
                player_inventory.append("Armor")
                player_room = "Armory"
                print(f"You are now wearing the armor you once used and went into the {player_room}")
                sleep(3)
                while True:
                    player_sword = input("You see a mounted sword that once belonged to you what do you do? [get sword/leave sword]: ")

                    if player_sword.lower() == "get sword":
                        player_inventory.append("Sword")
                        print("You are now weilding a trusty sword you must head back and find your way out...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)

                    elif player_sword.lower() == "leave sword":
                        print("You left your sword behind pondering of the consequences ahead...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)

                    else:
                        print("Please enter a valid option")
            elif player_armor.lower() == "leave armor":
                player_room = "Armory"
                print(f"You left your armor wondering if the consequenses will be dire as you head into the {player_room}.")
                while True:
                    player_sword = input("You see a mounted sword that once belonged to you what do you do? [get sword/leave sword]: ")

                    if player_sword.lower() == "get sword":
                        player_inventory.append("Sword")
                        print("You are now weilding a trusty sword without your armor, you must head back and find your way out...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)

                    elif player_sword.lower() == "leave sword":
                        print("You left your sword and armor behind pondering of the consequences ahead...")
                        start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)

                    else:
                        print("Please enter a valid option")
            else:
                print("please enter a valid option")

def eastern_messhall():
    print("You walk in and see an empty mess hall.")
    sleep(2)
    print("You wonder where everyone is at")
    sleep(2)
    print("You see your shield mounted as a trohpy")
    sleep(2)
    print("You wonder why they are doing so")
    sleep(2)
    player_room = "Eastern Messhall"
    while True:
        player_shield = input("You look at the what should you do? [get shield/leave shield]: ")
        if player_shield.lower() == "get shield":
            player_inventory.append("Shield")
            print("You have aquired your shield..")
            sleep(2)
            print("You must look for the rest of your items to escape..")
            eastern_hall_has_run = True
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif player_shield.lower() == "leave shield":
            print("You decided to not take your shield..")
            sleep(2)
            print("You decide to keep going.. was that a mistake?")
            eastern_hall_has_run = True
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")

def bedrooms():
    player_room = "Bedrooms"
    print(f"You enter the {player_room}. You only see dying sick woman and children.")
    sleep(2)
    print("You wonder where the men have gone")
    sleep(2)
    print("You go looking around and you see your helmet being worn by a corpse")
    sleep(2)
    print("You wonder why the had your helmet..")
    sleep(2)
    while True:
        player_shield = input("You look at the helmet what should you do? [get helmet/leave helmet]: ")
        if player_shield.lower() == "get helmet":
            player_inventory.append("Helmet")
            print("You have aquired your helmet..It smells foul but nothing you cant handle")
            sleep(2)
            print("You must look for the rest of your items to escape..")
            bedrooms_has_run = True
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif player_shield.lower() == "leave helmet":
            print("You decided to not take your helmet..its abosolutely disgusting")
            sleep(2)
            print("You decide to keep going.. will you need the helmet?")
            bedrooms_has_run = True
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")

def kitchen():
    print("You walk in and see an empty mess hall.")
    sleep(2)
    print("You wonder where everyone is at")
    sleep(2)
    print("You see your shield mounted as a trohpy")
    sleep(2)
    print("You wonder why they are doing so")
    sleep(2)
    player_room = "Eastern Messhall"
    while True:
        kitchen_has_run = True
        player_shield = input("You look at the what should you do? [get shield/leave shield]: ")
        if player_shield.lower() == "get shield":
            player_inventory.append("Shield")
            print("You have aquired your shield..")
            sleep(2)
            print("You must look for the rest of your items to escape..")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif player_shield.lower() == "leave shield":
            print("You decided to not take your shield..")
            sleep(2)
            print("You decide to keep going.. was that a mistake?")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")
def wizard_library():
    print("You walk in and see an empty mess hall.")
    sleep(2)
    print("You wonder where everyone is at")
    sleep(2)
    print("You see your shield mounted as a trohpy")
    sleep(2)
    print("You wonder why they are doing so")
    sleep(2)
    player_room = "Eastern Messhall"
    while True:
        wizard_library_has_run = True
        player_shield = input("You look at the what should you do? [get shield/leave shield]: ")
        if player_shield.lower() == "get shield":
            player_inventory.append("Shield")
            print("You have aquired your shield..")
            sleep(2)
            print("You must look for the rest of your items to escape..")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        elif player_shield.lower() == "leave shield":
            print("You decided to not take your shield..")
            sleep(2)
            print("You decide to keep going.. was that a mistake?")
            start(player_room, barracks_has_run, eastern_hall_has_run, bedrooms_has_run, kitchen_has_run, wizard_library_has_run)
        else:
            print("Please enter a valid option")

# Make sure file does not run when imported
if __name__ == "__main__":
    main_menu()
