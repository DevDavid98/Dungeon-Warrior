# David A Garcia III

# import any module thats required for the text based game 
import random
import pygame
from sys import exit
from time import sleep


player_map = {
        'Prison Cell':{"South": "Western Greathall"},

        'Western Greathall': {"North":"Prison Cell", "East": "Central Greathall"},
        'Central Greathall': {"West":"Western Greathall", "South":"Eastern Messhall", "North":"Gaurd Barracks", "East":"Eastern Greathall"},
        'Eastern Greathall': {"East":"Torture Chamber", "North":"Library of Wizardry"},

        'Library of Wizardry':{"South":"Eastern Greathall"},

        'Torture Chamber':{"West":"Eastern Greathall", "South":"Dragon Chamber"},
        'Dragon Chamber':{"North":"Torchure Chamber","West":"Grand Staircase"},

        'Gaurd Barracks': {"South":"Central Greathall", "East":"Armory"},
        'Armory':{"East":"Gaurd Barracks"},

        'Eastern Messhall':{"North":"Central Greathall", "South":"Bedrooms", "West": "Western Messhall"},
        'Western Messhall':{"South":"Kitchen","East":"Eastern Messhall"}

    }
barracks_has_run = False
player_inventory = []
current_room = "Prison Cell"
def player_controls():
        print("\n")
        print('To move directions type "North", "South", "East" or "West"')
        print('To grab a item type "get [item name]"')
        print('To quit the game type "exit"')

def main_menu():
    print("WELCOME TO DUNGEON WARRIOR")
    print("-"*26)
    while True:
        print("\nTo begin press 'S' to start game")
        print("To view controls press 'C'")
        user_input = input("\nEnter a valid command: ")
        if user_input.lower() == "s":
            start(current_room)
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

def start(player_room):
    objective = "Retrieve your items and escape"
    #backstory()
    print("-" * 60)
    print("You awaken in a dark cell trying to remember who you are..")
    sleep(3)
    player_name = input("What is your name?: ")
    print("-" * 60)
    #current_room = "Prison Cell"

    while True:
        print(f"{player_name}, you are currently in:", player_room)
        player_direction = input("Which way will you go?: ")
        print("\n")

        if player_direction.title() in player_map[player_room]:
            player_room = player_map[player_room][player_direction.title()]
            if player_room == "Gaurd Barracks":
                barracks()

        elif player_direction.lower() == "c":
            player_controls()
        elif player_direction.lower() == "exit":
            exit("Thank you for playing Dungeon Warrior")

        else:
            print("There's a wall in front of you. Try another way.\n")

def barracks():
    barracks_has_run = True
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

    player_decision = input("Choose your approach A/B: ")

    if player_decision.lower() == "a":
        sneak = random.randint(1,3)
        if sneak == 1:
            print("You have successfuly snuck passed the gaurds and enterd the amrory")
            

        elif sneak == 2:
            print("Oh no! the gaurds have found you. You must fight them!")
            sleep(3)
            print("The gaurds shocked that you were there beat you mercilessly with no remorse only to get tired")
            sleep(3)
            print("You notice this and take advantage of the situation")
            sleep(3)
            print("You end up defeating the gaurds with your fist barely escaping with your life")
            sleep(3)
            player_armor = input("You see your amror on the table [get armor/leave armor]: ")
            if player_armor.lower() == "get armor":
                player_inventory.append["Armor"]
                print("You are now wearing the armor you once used")
                sleep(3)
                current_room = "Armory"
                print(f"You see a door on your right, you enter only for it to be the {current_room}")
            if player_armor.lower() == "leave armor":
                current_room = "Armory"
                print(f"You see a door on your right, you enter only for it to be the {current_room}")


    elif player_decision.lower() == "b":
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
            player_inventory.append("Armor")
            print("You are now wearing the armor you once used")
            sleep(1)
            current_room = "Armory"
            print(f"You see a door on your right, you enter only for it to be the {current_room}")
        if player_armor.lower() == "leave armor":
            current_room = "Armory"
            print(f"You see a door on your right, you enter only for it to be the {current_room}")
    else:
        print("Please enter a valid option!")


# Make sure file does not run when imported
if __name__ == "__main__":
    main_menu()

